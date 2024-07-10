import axios from 'axios';

const API_URL = 'http://localhost:8000';  // Замените на ваш адрес сервера

export const createRoom = async () => {
    const response = await axios.post(`${API_URL}/create-room`);
    return response.data;
};

export const addPlayerToRoom = async (roomId: number, playerId: number) => {
    const response = await axios.post(`${API_URL}/add-player`, {
        roomId,
        playerId
    });
    return response.data;
};

export const startGame = async (roomId: number) => {
    const response = await axios.post(`${API_URL}/start-game`, { roomId });
    return response.data;
};

export const getGameState = async (roomId: number) => {
    const response = await axios.get(`${API_URL}/game-state`, { params: { roomId } });
    return response.data;
};
