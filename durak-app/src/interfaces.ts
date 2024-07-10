export interface Player {
    id: number;
    username: string;
 }
 
 export interface Room {
   id: number;
   players: Player[];
   max_players: number;
 }
 
 export interface ErrorResponse {
   message: string;
 }
 
 export interface CreateRoomRequest {
   room_id: number;
 }
 
 export interface JoinRoomRequest {
   id: number;
   username: string;
 }
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
 