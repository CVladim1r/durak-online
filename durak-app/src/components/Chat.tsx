import React, { useState } from 'react';

interface ChatProps {
    onSendMessage: (message: string) => void;
}

const Chat: React.FC<ChatProps> = ({ onSendMessage }) => {
    const [message, setMessage] = useState("");

    const sendMessage = () => {
        onSendMessage(message);
        setMessage("");
    };

    return (
        <div className="chat">
            <input 
                type="text" 
                value={message} 
                onChange={(e) => setMessage(e.target.value)} 
                placeholder="Type your message..." 
            />
            <button onClick={sendMessage}>Send</button>
        </div>
    );
};

export default Chat;
