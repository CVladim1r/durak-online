import React from 'react';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      userId: null,
      username: null,
    };
  }

  componentDidMount() {
    // Проверяем доступность Telegram.WebApp и initDataUnsafe
    if (window.Telegram && window.Telegram.WebApp && window.Telegram.WebApp.initDataUnsafe) {
      const { userId, username } = window.Telegram.WebApp.initDataUnsafe;
      this.setState({ userId, username });
    } else {
      console.error('Telegram.WebApp.initDataUnsafe is not available.');
    }
  }

  render() {
    const { userId, username } = this.state;
    return (
      <div className="App">
        <header className="App-header">
          {username ? (
            <p>Привет {username} (ID: {userId})</p>
          ) : (
            <p>Loading...</p>
          )}
        </header>
      </div>
    );
  }
}

export default App;
