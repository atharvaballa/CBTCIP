import React, { useState, useEffect } from 'react';
import GameBoard from './components/GameBoard';

function App() {
  const [numDigits, setNumDigits] = useState(4);
  const [gameId, setGameId] = useState(null);
  const [guesses, setGuesses] = useState([]);
  const [isGameOver, setIsGameOver] = useState(false);
  const [result, setResult] = useState('');

  const startGame = () => {
    fetch('/start_game', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ num_digits: numDigits })
    })
    .then(response => response.json())
    .then(data => {
      setGameId(data.game_id);
    });
  };

  const makeGuess = (guess) => {
    fetch('/make_guess', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ game_id: gameId, guess: guess })
    })
    .then(response => response.json())
    .then(data => {
      if (data.result === 'win') {
        setIsGameOver(true);
        setResult('You win!');
      } else if (data.result === 'lose') {
        setIsGameOver(true);
        setResult('You lose!');
      } else {
        setGuesses(prevGuesses => [...prevGuesses, { guess, ...data }]);
      }
    });
  };

  return (
    <div className="app">
      <h1>Mastermind</h1>
      <button onClick={startGame}>Start Game</button>
      {!isGameOver && <GameBoard guesses={guesses} makeGuess={makeGuess} />}
      {isGameOver && <p>{result}</p>}
    </div>
  );
}

export default App;
