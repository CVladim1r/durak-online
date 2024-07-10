import React, { useState, useEffect } from 'react';
import Api from '../api'; // Assuming Api is exported as default
import { Room, CreateRoomRequest, JoinRoomRequest } from './interfaces';

interface RoomsComponentProps {
  onRoomJoined: (roomId: number, playerId: number) => void;
}

const RoomsComponent: React.FC<RoomsComponentProps> = ({ onRoomJoined }) => {
  const [rooms, setRooms] = useState<number[]>([]); // Список доступных комнат
  const [roomId, setRoomId] = useState<number | null>(null); // Выбранный ID комнаты

  // Загрузка списка комнат при загрузке компонента
  useEffect(() => {
    fetchAllRooms();
  }, []);

  // Функция для получения списка всех комнат
  const fetchAllRooms = async () => {
    try {
      Api.getAllRooms(); // Вызов метода API для получения всех комнат
      // Ожидаем ответа от сервера через WebSocket
      Api.socket.addEventListener('message', (event) => {
        const data = JSON.parse(event.data);
        if (data.action === 'get_all_rooms') {
          setRooms(data.rooms);
        }
      });
    } catch (error) {
      console.error('Failed to fetch rooms:', error);
    }
  };

  // Функция для создания новой комнаты
  const handleCreateRoom = () => {
    const request: CreateRoomRequest = { /* данные для создания комнаты */ };
    api.createRoom(request); // Вызов метода API для создания комнаты
    // Ожидаем ответа от сервера через WebSocket
    api.socket.addEventListener('message', (event) => {
      const data = JSON.parse(event.data);
      if (data.action === 'create_room') {
        onRoomJoined(data.room_id, data.player_id);
      }
    });
  };

  // Функция для подключения к выбранной комнате
  const handleJoinRoom = () => {
    if (!roomId) {
      console.error('Room ID is not selected');
      return;
    }

    const request: JoinRoomRequest = { /* данные для присоединения к комнате */ };
    api.addPlayer(request); // Вызов метода API для присоединения к комнате
    // Ожидаем ответа от сервера через WebSocket
    api.socket.addEventListener('message', (event) => {
      const data = JSON.parse(event.data);
      if (data.action === 'add_player') {
        onRoomJoined(data.room_id, data.player_id);
      }
    });
  };

  return (
    <div>
      <h2>Rooms:</h2>
      <ul>
        {rooms.map(roomId => (
          <li key={roomId}>
            Room {roomId}{' '}
            <button onClick={() => setRoomId(roomId)}>Join</button>
          </li>
        ))}
      </ul>
      <button onClick={handleCreateRoom}>Create Room</button>
      <button onClick={handleJoinRoom} disabled={roomId === null}>
        Join Selected Room
      </button>
    </div>
  );
};

export default RoomsComponent;
