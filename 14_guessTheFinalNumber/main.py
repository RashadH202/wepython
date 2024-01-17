from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess: int, answer: int, turns: int) -> int:
    """Check the user's guess against the correct answer and update the remaining turns."""
    if guess > answer:
        print("Too High")
    elif guess < answer:
        print("Too Low")
    else:
        print(f"You got it! The answer was {answer}.")
        turns = 0  # Set turns to 0 to exit the loop when the answer is correct
    return turns

def set_difficulty() -> int:
    """Set the difficulty level and return the corresponding number of turns."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    return EASY_LEVEL_TURNS if level == "easy" else HARD_LEVEL_TURNS

def game():
    """Run the Number Guessing Game."""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    # For debugging purposes, you may want to comment out the line below in a complete version.
    print(f"Psst, the correct answer is {answer}")

    turns = set_difficulty()

    while turns > 0:
        print(f"You have {turns} attempts remaining to guess the number!")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You ran out of guesses. You lose!")

if __name__ == "__main__":
    game()
