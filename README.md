# Word-guessing-game-using-python
# Word Guessing Game

This is a simple command-line word guessing game written in Python. The game randomly selects a word from a predefined list and the player has to guess the characters of the word. The player has a limited number of guesses, and the goal is to guess the word before running out of attempts.

## Features:
- Random word selection from a predefined list.
- Allows the user to guess one letter at a time.
- The game provides feedback if the guessed letter is correct or wrong.
- The player has a limited number of guesses based on the length of the word.
- Replay option to play the game multiple times.
- Error handling for invalid input, ensuring the user enters a valid single alphabetic character.

## How to Play:
1. **Start the Game**: Upon running the game, you will be prompted to enter your name.
2. **Guess the Word**: The game will show the number of characters in the word and you have to guess the letters one by one.
3. **Make Guesses**: You can enter a single letter for each guess. If the letter is part of the word, it will be revealed.
4. **Limited Attempts**: You have a limited number of guesses. If you guess wrong, you lose one chance.
5. **Win or Lose**: You win the game if you guess all the letters in the word before running out of guesses. If you run out of guesses, you lose the game.
6. **Play Again**: After each game, you are asked if you want to play again.

## Installation:
To run this game on your local machine, make sure you have Python installed.

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/dhatsheth-roshan/python-projects/basic/word-guessing-game.git

## Code Explanation:
The game picks a random word from a list.
The player guesses letters one by one.
If the guess is correct, the letter is revealed in the word.
The number of remaining guesses is based on the length of the word.
The game ends when the player guesses the word or runs out of attempts.
The user is asked if they want to play again after each round.

## Dependencies:
No external libraries are required for this project. It uses only built-in Python libraries:

random
math


## Contributing:
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes. Please ensure that your contributions adhere to the project's coding standards.

## License:
This project is licensed under the MIT License - see the LICENSE file for details.
