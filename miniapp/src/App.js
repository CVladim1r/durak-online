import React from 'react';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: true, // Флаг загрузки данных
      error: null,   // Ошибка при загрузке данных, если есть
      userId: null,
      username: null,
    };
  }

  componentDidMount() {
    // Проверяем доступность Telegram.WebApp и initDataUnsafe
    if (window.Telegram && window.Telegram.WebApp && window.Telegram.WebApp.initDataUnsafe) {
      try {
        const { userId, username } = window.Telegram.WebApp.initDataUnsafe;
        this.setState({ userId, username, loading: false });
      } catch (error) {
        console.error('Error retrieving data:', error);
        this.setState({ error: 'Error retrieving data', loading: false });
      }
    } else {
      console.error('Telegram.WebApp.initDataUnsafe is not available.');
      this.setState({ error: 'Telegram.WebApp.initDataUnsafe is not available.', loading: false });
    }
  }

  render() {
    const { loading, error, userId, username } = this.state;

    if (loading) {
      return <p>Loading...</p>;
    }

    if (error) {
      return <p>Error: {error}</p>;
    }

    return (
      <div className="App">
        <header className="App-header">
          {username ? (
            <p>Привет {username} (ID: {userId})</p>
          ) : (
            <p>No username available</p>
          )}
        </header>
      </div>
    );
  }
}

export default App;
