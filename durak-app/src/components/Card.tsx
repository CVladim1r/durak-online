import React from 'react';

interface CardProps {
    card: string;
    onClick: () => void;
}

const Card: React.FC<CardProps> = ({ card, onClick }) => {
    return (
        <div onClick={onClick} className="card">
            {card}
        </div>
    );
};

export default Card;
