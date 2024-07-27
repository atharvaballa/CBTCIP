import axios from 'axios';

const apiBaseUrl = 'http://localhost:5000'; // Replace with your backend URL

const startGame = (numDigits) => {
  return axios.post(`${apiBaseUrl}/start_game`, { num_digits: numDigits });
};

const makeGuess = (gameId, guess) => {
  return axios.post(`${apiBaseUrl}/make_guess`, { game_id: gameId, guess: guess });
};

export { startGame, makeGuess };
