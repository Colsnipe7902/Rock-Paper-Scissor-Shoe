from random import choice

winning_message = {
    "rock": "Rock crushes scissors",
    "paper": "Paper covers rock",
    "scissors": "Scissors cut paper"
}

player_wins = 0
computer_wins = 0

player_art = '''
    Rock...
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

computer_art = '''
    ...Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

game_rules = """
Welcome to Rock, Paper, Scissors!

You'll be playing against the computer.
The rules are:
Rock wins against scissors
Scissors win against paper
Paper wins against rock

Let's play!
"""

print(game_rules)

while True:
    player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    if player_choice in ["rock", "paper", "scissors"]:
        computer_choice = choice(["rock", "paper", "scissors"])
        
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
            print(f"{player_choice.capitalize()} wins! {winning_message[player_choice]}")
            player_wins += 1
            print(player_art)
        else:
            print(f"{computer_choice.capitalize()} wins! {winning_message[computer_choice]}")
            computer_wins += 1
            print(computer_art)

        print(f"Player wins: {player_wins}, Computer wins: {computer_wins}")
        play_again = input("Play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Goodbye!")
            break
    else:
        print("Invalid input. Please try again.")
