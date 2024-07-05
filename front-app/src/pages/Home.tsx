// src/pages/Home.tsx
import React from 'react';
import { useTranslation } from 'react-i18next';
import { Button } from '@mui/material';
import { useNavigate } from 'react-router-dom';

const Home: React.FC = () => {
  const { t } = useTranslation();
  const navigate = useNavigate();

  return (
    <div>
      <h1>{t('welcome')}</h1>
      <Button variant="contained" color="primary" onClick={() => navigate('/profile')}>
        Go to Profile
      </Button>
    </div>
  );
};

export default Home;
