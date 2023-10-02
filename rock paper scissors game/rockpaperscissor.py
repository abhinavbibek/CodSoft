import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def display_choices(user_choice, computer_choice):
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

def display_score(user_score, computer_score):
    print(f"\nYour score: {user_score}")
    print(f"Computer's score: {computer_score}")

def display_game_summary(user_score, computer_score):
    print("\nGame Summary:")
    print(f"Total rounds played: {user_score + computer_score}")
    print(f"You won {user_score} rounds.")
    print(f"Computer won {computer_score} rounds.")
    if user_score > computer_score:
        print("Congratulations! You are the overall winner.")
    elif user_score < computer_score:
        print("Better luck next time! Computer is the overall winner.")
    else:
        print("It's a draw. No overall winner.")

print("Welcome to Rock, Paper, Scissors Game!")

user_score = 0
computer_score = 0

while True:
    print("\n--- New Round ---")
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("\nChoose rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    
    computer_choice = random.choice(choices)
    display_choices(user_choice, computer_choice)

    result = determine_winner(user_choice, computer_choice)
    print(f"\nResult: {result}")
    
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1

    display_score(user_score, computer_score)

    play_again = input("\nDo you want to play another round? (y/n): ").lower()
    if play_again != 'y':
        break

print("\n--- Game Over ---")
display_game_summary(user_score, computer_score)
