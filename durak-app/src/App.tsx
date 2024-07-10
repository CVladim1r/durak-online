import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import GamePage from './pages/GamePages';
import MarketPage from './pages/MarketPage';
import ProfilePage from './pages/ProfilePage';
import InfoPage from './pages/InfoPage';

const App: React.FC = () => {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<GamePage />} />
        <Route path="/market" element={<MarketPage />} />
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/info" element={<InfoPage />} />
      </Routes>
    </Router>
  );
};

export default App;
