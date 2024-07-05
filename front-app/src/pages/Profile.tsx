// src/pages/Profile.tsx
import React from 'react';
import { useSelector } from 'react-redux';
import { RootState } from '../store';

const Profile: React.FC = () => {
  const user = useSelector((state: RootState) => state.user);

  return (
    <div>
      <h1>Profile</h1>
      <p>User ID: {user.id}</p>
      <p>Username: {user.username}</p>
    </div>
  );
};

export default Profile;
