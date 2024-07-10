import React from 'react';
import { useNavigate } from 'react-router-dom';
import { createRoom } from '../utils/api';

const Home: React.FC = () => {
    const navigate = useNavigate();

    const createRoomHandler = async () => {
        const { roomId, playerId } = await createRoom();
        navigate(`/room/${roomId}/${playerId}`);
    };

    return (
        <div className="home">
            <button onClick={createRoomHandler}>Create Room</button>
        </div>
    );
};

export default Home;
