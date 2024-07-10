import React, { useState, useEffect } from 'react';
import axios from 'axios';

const GameBoard = ({ roomId, playerId }) => {
    const [roomInfo, setRoomInfo] = useState(null);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchRoomInfo = async () => {
            try {
                const response = await axios.get(`/room/${roomId}`);
                setRoomInfo(response.data);
            } catch (error) {
                setError(error.response.data.detail);
            }
        };

        if (roomId) {
            fetchRoomInfo();
        }
    }, [roomId]);

    const handlePlayCard = async (cardIndex) => {
        try {
            const response = await axios.post(`/room/${roomId}/play_card`, { player_id: playerId, card_index: cardIndex });
            setRoomInfo(response.data);
        } catch (error) {
            setError(error.response.data.detail);
        }
    };

    const renderGameInfo = () => {
        if (!roomInfo) {
            return <p>Loading...</p>;
        }

        return (
            <div>
                <h2>Game Board</h2>
                <p>Room ID: {roomInfo.id}</p>
                <p>Status: {roomInfo.status}</p>
                <p>Current Turn: Player {roomInfo.current_turn}</p>

                {roomInfo.players.map((player, index) => (
                    <div key={index}>
                        <h3>Player {player.id}</h3>
                        <p>Username: {player.username}</p>
                        <p>Hand:</p>
                        <ul>
                            {player.hand.map((card, cardIndex) => (
                                <li key={cardIndex}>
                                    {card.rank} of {card.suit}
                                    {roomInfo.current_turn === player.id && (
                                        <button onClick={() => handlePlayCard(cardIndex)}>Play Card</button>
                                    )}
                                </li>
                            ))}
                        </ul>
                    </div>
                ))}

                <h3>Table</h3>
                <p>Played Cards:</p>
                <ul>
                    {roomInfo.played_cards.map((card, cardIndex) => (
                        <li key={cardIndex}>{card.rank} of {card.suit}</li>
                    ))}
                </ul>

                {error && <p>Error: {error}</p>}
            </div>
        );
    };

    return (
        <div>
            {renderGameInfo()}
        </div>
    );
};

export default GameBoard;
