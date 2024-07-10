import { useEffect, useState } from 'react';

const ProfilePage: React.FC = () => {
    const [userData, setUserData] = useState<any>(null);

    useEffect(() => {
        const Telegram = (window as any).Telegram;
        if (Telegram && Telegram.WebApp && Telegram.WebApp.initDataUnsafe) {
            const userData = Telegram.WebApp.initDataUnsafe.user;
            setUserData(userData);
        }
    }, []);

    return (
        <div className="user-info">
            <h2>User Profile</h2>
            <p><strong>Name:</strong> {userData?.first_name} {userData?.last_name}</p>
            <p><strong>Username:</strong> @{userData?.username}</p>
            <p><strong>Language Code:</strong> {userData?.language_code}</p>
            <p><strong>User ID:</strong> {userData?.id}</p>
        </div>
    );
}

export default ProfilePage;
