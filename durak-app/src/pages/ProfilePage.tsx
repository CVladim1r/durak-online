import React, { useEffect, useState } from 'react';
import '../pages/_profilePage.scss';

const ProfilePage: React.FC = () => {
  const [userData, setUserData] = useState<any>({});

  useEffect(() => {
    const fetchData = async () => {
      try {
        await window.Telegram.WebApp.init();
        const userData = window.Telegram.WebApp.initDataUnsafe.user;
        setUserData(userData);
      } catch (error) {
        console.error('Error initializing Telegram WebApp:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="user-info">
      <h2>User Profile</h2>
      <p><strong>Name:</strong> {userData.first_name} {userData.last_name}</p>
      <p><strong>Username:</strong> @{userData.username}</p>
      <p><strong>Language Code:</strong> {userData.language_code}</p>
      <p><strong>User ID:</strong> {userData.id}</p>
    </div>
  );
};

export default ProfilePage;
