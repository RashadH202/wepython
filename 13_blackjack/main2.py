import random
from art import logo
from replit import clear

class BlackjackGame:
    def __init__(self):
        # Initialize the game with empty hands and game state
        self.user_cards = []
        self.computer_cards = []
        self.is_game_over = False

    def deal_card(self):
        # Return a randomly chosen card from the deck
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)

    def calculate_score(self, cards):
        # Calculate the total score of a hand
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        
        return sum(cards)

    def compare(self, user_score, computer_score):
        # Compare scores and determine the winner
        if user_score > 21 and computer_score > 21:
            return "You went over. You lose."
        elif user_score == computer_score:
            return "It's a draw."
        elif computer_score == 0:
            return "You win with a blackjack!"
        elif user_score == 0:
            return "You win with a blackjack!"
        elif user_score > 21:
            return "You went over. You lose."
        elif computer_score > 21:
            return "You win!"
        elif user_score > computer_score:
            return "You win!"
        else:
            return "You lose!"

    def play_game(self):
        # Start a new round of the game
        self.user_cards = [self.deal_card() for _ in range(2)]
        self.computer_cards = [self.deal_card() for _ in range(2)]
        self.is_game_over = False

        while not self.is_game_over:
            # Display current game status
            self.display_status()
            # Allow the user to take their turn
            self.user_turn()

        # Let the computer play its turn
        self.computer_turn()
        # Display the final result of the round
        self.display_final_result()

    def user_turn(self):
        # Allow the user to take their turn
        user_score = self.calculate_score(self.user_cards)
        computer_score = self.calculate_score(self.computer_cards)

        if user_score == 0 or computer_score == 0 or user_score > 21:
            self.is_game_over = True
        else:
            try:
                user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if user_should_deal == "y":
                    self.user_cards.append(self.deal_card())
                elif user_should_deal != "n":
                    raise ValueError("Invalid input. Please enter 'y' or 'n'.")
                else:
                    self.is_game_over = True
            except ValueError as e:
                print(e)

    def computer_turn(self):
        # Allow the computer to take its turn
        while self.calculate_score(self.computer_cards) != 0 and self.calculate_score(self.computer_cards) < 17:
            self.computer_cards.append(self.deal_card())

    def display_status(self):
        # Display the current game status
        print(f"Your cards: {self.user_cards}, current score: {self.calculate_score(self.user_cards)}")
        print(f"Computer's first card: {self.computer_cards[0]}")

    def display_final_result(self):
        # Display the final result of the round
        print(f"Your final hand: {self.user_cards}. Final score: {self.calculate_score(self.user_cards)}")
        print(f"Computer's final hand: {self.computer_cards}. Final score: {self.calculate_score(self.computer_cards)}")
        print(self.compare(self.calculate_score(self.user_cards), self.calculate_score(self.computer_cards)))

if __name__ == "__main__":
    # Start the game
    clear()
    game = BlackjackGame()
    while input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower() == "y":
        clear()
        game.play_game()
