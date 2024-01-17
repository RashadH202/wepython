from game_data import data
import random
from art import logo, vs
from replit import clear
def get_random_account():
    """"Return a random acount from the data"""
    return random.choice(data)

def format_data(account):
    """format the account data for display"""
    name, description, country = account["name"], account ["description"], account["country"]
    return f"{name}, a {description}, from {country}"

def display_accounts(account_a, account_b):
    """display the comparison between two accounts"""
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

def get_user_guess():
    """"get the users guess and validate input"""
    while True:
        guess = input("Who has more followers? type a or b?:").lower()
        if guess in ['a', 'b']:
            return guess
        else:
            print("invalid input. please type a or b")

def check_answer(guess, a_followers, b_followers):
    """check if the users guess is correct"""
    return(guess == "a" and a_followers > b_followers)  or (guess == "b" and b_followers > a_followers)

def game():
    """run the main game loop"""
print(logo)

score = 0

game_should_continue = True
account_a = get_random_account()
account_b = get_random_account()

while game_should_continue:
    account_a, account_b = account_b, get_random_account()
    while account_a == account_b:
        account_a, account_b = account_b, get_random_account()

    display_accounts(account_b, account_b)

    guess = get_user_guess()
    a_follower_count, b_follower_count = account_a["follower_count"], account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()

    if is_correct:
        score += 1
        print(f"you're right! current score: {score}")
    else:
        game_should_continue = False
        print(f"sorry, that's wrong. final score: {score}")
"""This block of code will be executed only if   the script is run directly,
not when it is imported as a module into another script."""
if __name__ == "__main__":
    game()