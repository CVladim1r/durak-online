import React from 'react';
import { useParams } from 'react-router-dom';
import GameBoard from '../components/GameBoard';
import Chat from '../components/Chat';

const GameRoom: React.FC = () => {
    const { roomId, playerId } = useParams<{ roomId: string, playerId: string }>();

    if (!roomId || !playerId) {
        return <div>Error: Room ID or Player ID is missing</div>;
    }

    const sendMessage = (message: string) => {
        // Send chat message to WebSocket
    };

    return (
        <div className="game-room">
            <GameBoard roomId={parseInt(roomId)} playerId={parseInt(playerId)} />
            <Chat onSendMessage={sendMessage} />
        </div>
    );
};

export default GameRoom;
