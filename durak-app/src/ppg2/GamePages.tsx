import React, { useState } from 'react';
import GameC from '../pp2-components/GameBoard';
import RoomsComponent from '../pp2-components/RoomsComponent';

const App: React.FC = () => {
  const [currentRoomId, setCurrentRoomId] = useState<number | null>(null);
  const [currentPlayerId, setCurrentPlayerId] = useState<number | null>(null);

  const handleRoomJoined = (roomId: number, playerId: number) => {
    setCurrentRoomId(roomId);
    setCurrentPlayerId(playerId);
  };

  return (
    <div>
      {!currentRoomId ? (
        <RoomsComponent onRoomJoined={handleRoomJoined} />
      ) : (
        <GameC roomId={currentRoomId} playerId={currentPlayerId} />
      )}
    </div>
  );
};

export default App;
