import React from 'react';
import { Link } from 'react-router-dom';
import '../components/_navbar.scss';

const Navbar: React.FC = () => {
  return (
    <nav>
      <ul>
        <li><Link to="/">Игра</Link></li>
        <li><Link to="/market">Маркет</Link></li>
        <li><Link to="/profile">Профиль</Link></li>
        <li><Link to="/info">Инфо</Link></li>
      </ul>
    </nav>
  );
};

export default Navbar;
