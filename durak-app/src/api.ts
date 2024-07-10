import { CreateRoomRequest, JoinRoomRequest } from './interfaces';

const backendUrl = 'ws://localhost:8000/ws';

export interface ApiMethods {
  createRoom(request: CreateRoomRequest): void;
  addPlayer(request: JoinRoomRequest): void;
  startGame(roomId: number): void;
  playCard(roomId: number, cardIndex: number): void;
  endTurn(roomId: number): void;
  getRoomInfo(roomId: number): void;
  getAllRooms(): void;
  sendChatMessage(roomId: number, message: string): void;
  getPlayerInfo(roomId: number, playerId: number): void;
  deleteRoom(roomId: number): void;
  getGameState(roomId: number): void;
  endGame(roomId: number): void;
  defend(roomId: number, defendingCardIndex: number): void;
}

class Api {
  private socket: WebSocket;

  constructor() {
    this.socket = new WebSocket(backendUrl);
    this.socket.addEventListener('open', () => {
      console.log('WebSocket connected');
    });
    this.socket.addEventListener('close', () => {
      console.log('WebSocket disconnected');
    });
    this.socket.addEventListener('error', (error) => {
      console.error('WebSocket error:', error);
    });
  }

  // Private method to send messages over WebSocket
  private sendMessage(message: any) {
    if (this.socket.readyState === WebSocket.OPEN) {
      this.socket.send(JSON.stringify(message));
    } else {
      console.error('WebSocket not connected');
    }
  }

  // Method to create a room
  createRoom(request: CreateRoomRequest) {
    this.sendMessage({
      action: 'create_room',
      ...request
    });
  }

  // Method to add a player to a room
  addPlayer(request: JoinRoomRequest) {
    this.sendMessage({
      action: 'add_player',
      ...request
    });
  }

  // Method to start the game in a room
  startGame(roomId: number) {
    this.sendMessage({
      action: 'start_game',
      room_id: roomId
    });
  }

  // Method for a player to play a card in a room
  playCard(roomId: number, cardIndex: number) {
    this.sendMessage({
      action: 'play_card',
      room_id: roomId,
      card_index: cardIndex
    });
  }

  // Method to end a turn in a room
  endTurn(roomId: number) {
    this.sendMessage({
      action: 'end_turn',
      room_id: roomId
    });
  }

  // Method to get information about a room
  getRoomInfo(roomId: number) {
    this.sendMessage({
      action: 'get_room_info',
      room_id: roomId
    });
  }

  // Method to get all available rooms
  getAllRooms() {
    this.sendMessage({
      action: 'get_all_rooms'
    });
  }

  // Method to send a chat message in a room
  sendChatMessage(roomId: number, message: string) {
    this.sendMessage({
      action: 'chat_message',
      room_id: roomId,
      message: message
    });
  }

  // Method to get information about a player in a room
  getPlayerInfo(roomId: number, playerId: number) {
    this.sendMessage({
      action: 'get_player_info',
      room_id: roomId,
      player_id: playerId
    });
  }

  // Method to delete a room
  deleteRoom(roomId: number) {
    this.sendMessage({
      action: 'delete_room',
      room_id: roomId
    });
  }

  // Method to get the current game state in a room
  getGameState(roomId: number) {
    this.sendMessage({
      action: 'get_game_state',
      room_id: roomId
    });
  }

  // Method to end the game in a room
  endGame(roomId: number) {
    this.sendMessage({
      action: 'end_game',
      room_id: roomId
    });
  }

  // Method for a player to defend against an attack in a room
  defend(roomId: number, defendingCardIndex: number) {
    this.sendMessage({
      action: 'defend',
      room_id: roomId,
      defending_card_index: defendingCardIndex
    });
  }
}

export default Api;
