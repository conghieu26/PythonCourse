import random

options = ["rock", "paper", "scissors"]


is_running =  True

while is_running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice (rock, paper, scissors): ")

        print(f"player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("It's a draw!")
        elif player == "rock" and computer == "scissors":
            print("You win!")
        elif player == "paper" and computer == "rock":
            print("You win!")
        elif player == "scissors" and computer == "paper":
            print("You win!")
        else:
            print("you lose!")

    if not input("Do you want to play again? (y/n): ").lower()== "y":
        is_running = False


print("Thanks for playing!")
