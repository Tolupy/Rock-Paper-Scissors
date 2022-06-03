
import random
R = "Rocks"
P = "Paper"
S = "Scissors"
possible_action = [R, P, S]

while True:

    player = input("Enter a choice: Rocks, Paper and Scissors: \n")
    computerAction = random.choice(possible_action)

    print(f" player'{(player)}:computer'{(computerAction)}")

    if player == computerAction:
        print(f" player'{(player)}:computer'{(computerAction)} and it's a tie")
    elif player == R:
        if computerAction == S:
            print("Rock beats Scissors!, You win!")
        else:
            print("Paper beats Rock!, You lose!")
    elif player == S:
        if computerAction == P:
            print("Scissors beat paper!, You win!")
        else:
            print("Rock beat Scissors!, You lose!")
    elif player == P:
        if computerAction == R:
            print("Paper beat Rock!, You win!")
        else:
            print("Scissors beat Paper!, You lose!")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

