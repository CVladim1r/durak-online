import React, { useState, useEffect } from 'react';
import Card from './Card';
import { connectToWebSocket } from '../websocket';
import { startGame, getGameState } from '../utils/api';

interface GameBoardProps {
    roomId: number;
    playerId: number;
}

const GameBoard: React.FC<GameBoardProps> = ({ roomId, playerId }) => {
    const [cards, setCards] = useState<string[]>([]);
    const [playedCards, setPlayedCards] = useState<string[]>([]);
    const [currentTurn, setCurrentTurn] = useState<number | null>(null);

    useEffect(() => {
        const socket = connectToWebSocket(roomId, playerId);

        socket.onmessage = (event) => {
            const message = JSON.parse(event.data);
            handleWebSocketMessage(message);
        };

        return () => {
            socket.close();
        };
    }, [roomId, playerId]);

    const handleWebSocketMessage = (message: any) => {
        switch (message.action) {
            case 'game_state':
                setCards(message.cards);
                setPlayedCards(message.played_cards);
                setCurrentTurn(message.current_turn);
                break;
            // Add more cases to handle other actions
        }
    };

    const startGameHandler = async () => {
        await startGame(roomId);
        const gameState = await getGameState(roomId);
        setCards(gameState.cards);
        setPlayedCards(gameState.played_cards);
        setCurrentTurn(gameState.current_turn);
    };

    const playCard = (cardIndex: number) => {
        // Send play_card action to WebSocket
    };

    return (
        <div className="game-board">
            <button onClick={startGameHandler}>Start Game</button>
            <div className="played-cards">
                {playedCards.map((card, index) => (
                    <Card key={index} card={card} onClick={() => {}} />
                ))}
            </div>
            <div className="hand-cards">
                {cards.map((card, index) => (
                    <Card key={index} card={card} onClick={() => playCard(index)} />
                ))}
            </div>
        </div>
    );
};

export default GameBoard;
