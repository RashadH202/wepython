# wepython - Learning Python

We are learning python one project at a time, I'll have descriptions of everything here if you want to reference anything i'll do my best to number each project. If you want to follow along, and try them yourself feel free to get it done !

# # CarGame - Project 1

A simple car racing game built using the Pygame library in Python.

## Features

- Player can control the car using the left and right arrow keys.
- Responsive car movement on the game canvas.
- Basic collision detection with the game window boundaries.
- Background image for a visually appealing game environment.
- Game loop to continuously update and display the game state.
- Smooth animation with a frame rate of 60 frames per second.

## Instructions

1. Ensure you have Python installed.
2. Install the Pygame library using `pip install pygame`.
3. Run the game by executing the provided Python script (`car_game.py`).
4. Use the left and right arrow keys to control the car.
5. Enjoy the simple car racing experience!

Feel free to modify and enhance the game as needed.


# # CarGame2 - Project 2

A simple car racing game implemented in Python using the Pygame library.

## Features

- Control your car using the left and right arrow keys.
- Avoid collisions with other vehicles on the road.
- Gain points for passing other vehicles.
- The game speeds up as you accumulate more points.
- Game over when there's a collision or when the player decides to quit.
- Responsive and smooth gameplay.

## How to Play

1. Ensure you have Python installed on your machine.
2. Install the Pygame library by running: `pip install pygame`.
3. Run the game by executing the provided Python script: `python car_game.py`.
4. Use the left and right arrow keys to control your car.
5. Avoid collisions with other vehicles and accumulate points.

## Controls

- **Left Arrow Key:** Move the car to the left lane.
- **Right Arrow Key:** Move the car to the right lane.
- **Enter Key (When Game Over):** Restart the game.

## Dependencies

- Python 3.x
- Pygame library

# # runescape reactFlask - Project 3

# Flask API for RuneScape Item Data

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description

This is a simple Flask API that fetches data about a RuneScape item using the official RuneScape API. The API endpoint `/` returns JSON data containing details about the specified RuneScape item.

## Prerequisites

Make sure you have the following installed before running the application:

- Python
- Flask
- Requests
- Flask-CORS
- pip install Flask requests flask-cor

You can install the dependencies using:

# # spotify reactFlask - project 4

### Flask Spotify App

A simple Flask web application that uses the Spotify API to interact with a user's Spotify account, allowing them to view playlists, see currently playing tracks, and get information about their Spotify account.

## Features

- Spotify authentication using the Spotify OAuth flow.
- Fetches and displays the user's playlists.
- Retrieves and shows the currently playing track.
- Displays information about the current user.

## Setup

1. Install the required Python packages using `pip install -r requirements.txt`.
2. Create a `.env` file in the project directory and add your Spotify API credentials:

   ```env
   -- SPOTIPY_CLIENT_ID=your_client_id
   -- SPOTIPY_CLIENT_SECRET=your_client_secret
   -- SPOTIPY_REDIRECT_URI=your_redirect_uri


# # tip Calculator - project 5

# Tip Calculator

A simple Python script that calculates the total bill amount, including tip, and splits it among the specified number of people.

## Usage

1. Run the script:

   ```bash
   python tip_calculator.py
# Tip Calculator

A simple Python script that calculates the total bill amount, including tip, and splits it among the specified number of people.

## Usage

1. Run the script:

   ```bash
   python tip_calculator.py

Welcome to the Tip Calculator!

What was the total bill? $100.00
How much tip would you like to give? 10, 12, 15? Just a number, please! 12
How many people to split the bill? 5

Total bill with tip: $112.00
Each person should pay: $22.40

### How It Works
The script takes input for the total bill amount, tip percentage, and the number of people. It calculates the total bill with the tip and then divides it equally among the specified number of people.

Feel free to modify the script or contribute to enhance its functionality. Happy calculating!

# Treasure Island Adventure

Welcome to the Treasure Island Adventure! Your mission is to find the mystical bear and navigate through a series of choices. Beware, as your decisions will determine your fate!

## How to Play

1. Run the script:

   ```bash
   python treasure_island.py

Welcome to Treasure Island!

Your mission is to find the mystical bear!

You're at a crossroad, where do you want to go? Type "left" or "right". left

You've come to a lake. There is an island in the middle of the lake. Type "wait" or "right". wait

You've reached the island. There is an island in the middle of the lake. Type "wait", "run across the lake", or "run along the shoreline"? run along the shoreline

The bear creeps up, and bites your arm off.

# Rock Paper Scissors ASCII Artn - Project 7

A simple Rock Paper Scissors game with ASCII art representation.

## Description

This program allows the user to play Rock Paper Scissors against a computer. The choices are represented with ASCII art for a fun visual experience.

## Usage

1. Run the script.
2. Enter your choice:
   - Type `0` for Rock
   - Type `1` for Paper
   - Type `2` for Scissors

3. The computer will randomly select its choice.
4. The program will display the ASCII art representing the choices.
5. The winner will be determined based on the game rules.

## ASCII Art

- **Rock:**
    ```
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ```

- **Paper:**
    ```
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    ```

- **Scissors:**
    ```
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    ```

## Rules

- Rock crushes Scissors
- Scissors cuts Paper
- Paper covers Rock

Have fun playing the game!

# Password Generator - Project 8

Generate a secure password using a combination of letters, numbers, and symbols.

## Description

This Python script generates a random password based on user-defined criteria, including the number of letters, symbols, and numbers.

## Usage

1. Run the script.
2. Enter the desired number of:
   - Letters
   - Symbols
   - Numbers

3. The script will generate a password combining letters, symbols, and numbers based on your input.
4. The generated password is shuffled for added security.

## Password Criteria

- **Letters:** The password may contain both lowercase and uppercase letters.
- **Numbers:** Numeric characters are included in the password.
- **Symbols:** Special symbols such as !, #, $, %, &, (, ), *, + may be included.

## How It Works

1. The user provides the desired number of letters, symbols, and numbers.
2. The script randomly selects characters from the predefined sets (letters, symbols, numbers).
3. The characters are combined into a list and shuffled.
4. The shuffled list is converted back to a string, forming the final password.

## Example

```python
Welcome to the PyPassword Generator!

How many letters would you like in your password? 8
How many symbols would you like? 2
How many numbers would you like? 2

Generated Password: jL$2hE8fP

# Hangman Game - Project 9

Play the classic Hangman game and guess the word before running out of lives!

## Description

This Python script allows you to play the Hangman game. A random word is selected from a predefined list, and you must guess the letters to uncover the word. Be careful not to run out of lives!

## Usage

1. Run the script.
2. The game will randomly choose a word from the word list.
3. You have 6 lives to guess the correct letters in the word.
4. Input a letter when prompted.
5. The script will display the current state of the word and the hangman figure.
6. Continue guessing until you either guess the word or run out of lives.

## Features

- **Word Selection:** The script randomly selects a word from a predefined list.
- **Lives:** You start with 6 lives, and you lose a life for each incorrect guess.
- **Visual Feedback:** The script displays the current state of the word and a hangman figure representing your remaining lives.

## How It Works

1. A word is randomly chosen from the word list.
2. You are prompted to input a letter guess.
3. The script updates the displayed word based on your guess.
4. Lives are deducted for incorrect guesses.
5. The game continues until you either guess the word or run out of lives.

## Example


```python
Welcome to Hangman!

_ _ _ _ _ _

Guess a letter: a
_ _ _ _ a _

Guess a letter: e
_ _ e _ a _

...

Guess a letter: t
t r e e a t

You win!

# Caesar Cipher - Project 10

Encrypt and decrypt messages using the classic Caesar Cipher technique with this Python script!

## Description

This Python script implements the Caesar Cipher algorithm to either encrypt or decrypt messages based on user input. The Caesar Cipher is a simple substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Usage

1. Run the script.
2. Choose to 'encode' or 'decode' a message.
3. Input the text message you want to process.
4. Specify the shift number for encryption/decryption.
5. The script will display the result based on your input.

## Features

- **Encode/Decode:** Choose whether to encode or decode a message.
- **Shift Amount:** Input the shift number to determine the level of encryption/decryption.
- **Alphabet Loop:** The alphabet wraps around, allowing for shifts beyond the standard 26 letters.

## How It Works

1. The script initializes an alphabet list containing both uppercase and lowercase letters.
2. The user inputs the direction ('encode' or 'decode'), the text message, and the shift amount.
3. The script processes the message using the Caesar Cipher algorithm.
4. The result is displayed based on the chosen direction.

## Example

```python
Welcome to the Caesar Cipher!

Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello
Type the shift number:
3

Here's the encoded result: khoor


# Silent Auction - Project 11

Manage a silent auction and find the highest bidder with this Python script!

## Description

This Python script allows users to conduct a silent auction by collecting bids from participants and determining the highest bidder. The script utilizes a dictionary to store participant names and their corresponding bid amounts.

## Usage

1. Run the script.
2. Enter participant names and their bid amounts.
3. Indicate whether there are additional bidders.
4. Once all bids are collected, the script will announce the winner and their bid.

## Features

- **Input Validation:** Ensures that bid amounts are valid numbers.
- **Winner Determination:** Finds and displays the highest bidder at the end of the auction.

## How It Works

1. The script initializes an empty dictionary (`bids`) to store participant names and bid amounts.
2. Users enter their name and bid amount.
3. The script adds the bid to the dictionary.
4. Participants are asked if there are additional bidders.
5. The highest bidder is determined once bidding is complete.

## Example

```python
Welcome to the Silent Auction!

What is your name?:
John
What is your bid?: $500
Are there any other bidders? Type 'yes' or 'no':
yes

Clearing the screen...

What is your name?:
Alice
What is your bid?: $700
Are there any other bidders? Type 'yes' or 'no':
no

The winner is Alice with a bid of $700


# Calculator - Project 12

Perform basic mathematical operations with this Python calculator script! The script allows users to add, subtract, multiply, and divide numbers interactively.

## Description

This Python calculator script provides a user-friendly interface for performing mathematical operations. Users can input two numbers and choose from a set of operations to calculate the result. The script includes basic error handling, such as preventing division by zero.

## Features

- **Addition:** Add two numbers.
- **Subtraction:** Subtract the second number from the first.
- **Multiplication:** Multiply two numbers.
- **Division:** Divide the first number by the second (avoiding division by zero).

## Usage

1. Run the script.
2. Enter the first number.
3. Choose an operation from the available options.
4. Enter the second number.
5. View the result and decide whether to continue with the result or start a new calculation.

## How It Works

1. The script defines functions for each mathematical operation (add, subtract, multiply, divide).
2. Users input the first number.
3. Users select an operation from the available options.
4. Users input the second number.
5. The script performs the chosen operation and displays the result.
6. Users decide whether to continue with the result or start a new calculation.

## Example

```python
Calculator

What's the first number?: 5
+   -   *   /

Pick an operation: +
What's the next number?: 3
5.0 + 3.0 = 8.0

Type 'y' to continue calculating with 8.0, or type 'n' to start a new calculation: y

Pick an operation: *
What's the next number?: 2
8.0 * 2.0 = 16.0

Type 'y' to continue calculating with 16.0, or type 'n' to start a new calculation: n


# Blackjack Game - Project 13

Welcome to the Blackjack Game! Play a game of Blackjack against the computer and try to get as close to 21 as possible without going over. Enjoy the thrill of making strategic decisions to beat the dealer.

## Description

This Python script allows users to play Blackjack in the console. The game includes features such as dealing cards, calculating scores, and determining the winner based on Blackjack rules. The user can decide whether to draw additional cards or pass, while the computer follows a set of rules for its turn.

## Features

- **Dealing Cards:** Randomly deal cards from the deck.
- **Calculating Scores:** Calculate the total score of a hand, considering Ace as 1 or 11.
- **Comparing Scores:** Determine the winner based on Blackjack rules.
- **Interactive Gameplay:** Allow users to choose whether to draw another card or pass.
- **Clear Console:** Use the `replit` library to clear the console for a cleaner interface.

## Usage

1. Run the script.
2. Type 'y' to play a game of Blackjack or 'n' to exit.
3. Follow the prompts to draw additional cards or pass.
4. See the final hands and scores at the end of the game.
5. Choose whether to play again.

## How It Works

1. The script defines functions for dealing cards, calculating scores, and comparing scores.
2. Users decide whether to draw another card or pass during their turn.
3. The computer follows a set of rules for its turn, drawing cards until its score is at least 17.
4. The script determines the winner based on the final scores.
5. Users can choose to play another round or exit the game.

## Example

```python
Blackjack Game

Do you want to play a game of blackjack? Type 'y' or 'n': y

Your cards: [10, 3], current score: 13
Computer's first card: 10
Type 'y' to get another card, type 'n' to pass: y
Your cards: [10, 3, 1], current score: 14
Computer's first card: 10
Type 'y' to get another card, type 'n' to pass: y
Your cards: [10, 3, 1, 6], current score: 20
Computer's first card: 10
Type 'y' to get another card, type 'n' to pass: n
Your final hand: [10, 3, 1, 6]. Final score: 20
Computer's final hand: [10, 5, 8]. Final score: 23
You win!
Do you want to play a game of blackjack? Type 'y' or 'n': n

# Number Guessing Game - Project 14

Welcome to the Number Guessing Game! Test your guessing skills by trying to find the correct number within a specified range. Adjust the difficulty level to challenge yourself or make it easier.

## Description

This Python script implements a simple Number Guessing Game. The program generates a random number between 1 and 100, and the player must guess the correct number within a limited number of attempts. The difficulty level can be set to 'easy' or 'hard,' with different numbers of allowed guesses.

## Features

- **Random Number Generation:** The game generates a random number between 1 and 100.
- **Difficulty Levels:** Choose between 'easy' (10 guesses) and 'hard' (5 guesses).
- **Interactive Gameplay:** Players input their guesses, and the game provides feedback on whether the guess is too high, too low, or correct.
- **Win/Lose Conditions:** The game ends when the player correctly guesses the number or runs out of attempts.

## Usage

1. Run the script.
2. Choose the difficulty level by typing 'easy' or 'hard.'
3. Make guesses by entering numbers.
4. Receive feedback on each guess.
5. Win the game by correctly guessing the number or lose when running out of attempts.
6. Optionally, the correct answer can be displayed for debugging purposes.

## How It Works

1. The program generates a random number between 1 and 100.
2. Players choose the difficulty level, determining the number of allowed guesses.
3. Players input guesses, and the game provides feedback.
4. The game continues until the correct number is guessed or the player runs out of attempts.

## Example

```python
Number Guessing Game

Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Psst, the correct answer is 42
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number!
Make a guess: 50
Too High
You have 9 attempts remaining to guess the number!
Make a guess: 30
Too Low
You have 8 attempts remaining to guess the number!
Make a guess: 42
You got it! The answer was 42.

# Higher Lower Game - Project 15

Welcome to the Higher Lower Game! Test your knowledge of follower counts on social media by choosing which account has more followers. Compare different accounts and see how high you can score!

## Description

This Python script implements the Higher Lower Game. The game displays two random social media accounts, and the player must guess which account has more followers. The score increases for each correct guess, and the game ends when the player makes an incorrect guess.

## Features

- **Random Account Generation:** The game selects two random social media accounts for comparison.
- **User Input Validation:** Ensure the user inputs a valid guess ('a' or 'b').
- **Scoring System:** Keep track of the player's score based on correct guesses.
- **Interactive Gameplay:** Players choose between two accounts and receive immediate feedback on their guesses.

## Usage

1. Run the script.
2. The game displays two social media accounts for comparison.
3. Choose 'a' or 'b' to guess which account has more followers.
4. Receive immediate feedback on your guess.
5. The game continues until you make an incorrect guess.
6. Your final score is displayed at the end of the game.

## How It Works

1. Two random social media accounts are selected for comparison.
2. Players choose between 'a' or 'b' to guess which account has more followers.
3. The game checks the guess and updates the score accordingly.
4. The game continues, displaying new accounts, until the player makes an incorrect guess.

## Example

```python
Higher Lower Game

Compare A: John Doe, a famous actor, from USA
Vs.
Against B: Jane Smith, a popular singer, from Canada
Who has more followers? Type 'a' or 'b': a
You're right! Current score: 1

Compare A: Jane Smith, a popular singer, from Canada
Vs.
Against B: Michael Johnson, a renowned chef, from UK
Who has more followers? Type 'a' or 'b': b
You're right! Current score: 2

...

Sorry, that's wrong. Final score: 7
