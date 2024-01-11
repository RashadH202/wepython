# Rock Paper Scissors ASCII Art

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissors = '''
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock,paper,scissors]

user_choice = int(input("what do you choice? type 0 for rock, 1 for paper, or 2 scisoors.\n"))
if user_choice >= 3 or user_choice <= -1:
    print("Invalid choice")
else:
    computer_choice = random.randint(0,2)

    print(game_images[computer_choice])
    print(game_images[user_choice])
    if user_choice == computer_choice:
        print("you draw")
    elif user_choice == 0 and computer_choice == 2:
        print("you win")
    elif user_choice == 0 and computer_choice == 1:
        print("you lose")
    elif user_choice == 1 and computer_choice == 0:
        print("you win")
    elif user_choice == 1 and computer_choice == 2:
        print("you lose")
    elif user_choice == 2 and computer_choice == 1:
        print("you win")
    elif user_choice == 2 and computer_choice == 0:
        print("you lose")
    else:
        print(f"computer chose {computer_choice}")