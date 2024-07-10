import React, { useEffect } from 'react';
import { io, Socket } from 'socket.io-client';

const GameC: React.FC = () => {
  useEffect(() => {
    const socket: Socket = io(); // Connect to the same domain
    // Use socket for further operations
    return () => {
      socket.disconnect(); // Clean up on unmount
    };
  }, []);

  return (
    <div>
      <h1>Игра</h1>
      {/* Логика игры */}
    </div>
  );
};

export default GameC;
