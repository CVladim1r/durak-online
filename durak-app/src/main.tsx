import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './_global.scss';

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <script src="https://telegram.org/js/telegram-web-app.js"></script> 

    <App />
    
  </React.StrictMode>,
);
