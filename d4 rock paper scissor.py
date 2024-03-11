import random


def game_logic(user_choice, computer_choice):
    """
    Determines the winner of a single round of Rock, Paper, Scissors.

    Args:
        user_choice (str): The user's choice ('rock', 'paper', or 'scissors').
        computer_choice (str): The computer's randomly generated choice.

    Returns:
        bool: True if the user wins, False if the user loses.
    """
    # Normalize user input to lowercase
    user_choice = user_choice.lower()

    # Define valid choices
    valid_choices = ['rock', 'paper', 'scissors']

    # Check if user input is valid
    if user_choice not in valid_choices:
        return "Invalid choice. Please choose 'rock', 'paper', or 'scissors'."

    # Determine winner based on rules
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return True  # User wins
    else:
        return False  # User loses

# Rock Paper Scissors ASCII Art

Rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
Scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_elements = {
    "rock": Rock,
    "paper": Paper,
    "scissors": Scissors
}

my_list = ["rock", "paper", "scissors"]
print('''What do you want to choose? type "rock","paper","scissors".....''')
user_choice = input()
print(f"You have choosen {user_choice}\n")
print(game_elements[user_choice])

computer_choice = random.choice(my_list)
print(f"computuer choosen {computer_choice}")
print(game_elements[computer_choice])

if computer_choice == user_choice:
    print("This game is a draw")
elif game_logic(user_choice,computer_choice):
    print("You have win")
else:
    print("You have lost")
