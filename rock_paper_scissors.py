import colorama
from colorama import Fore
import random
colorama.init()


rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_score = 0
computer_score = 0

play_again = True
while play_again:
    print(Fore.GREEN + "Let the 'Rock, Paper or Scissors' game begin!!")
    print(Fore.CYAN + "Now choose: [1]Rock, [2]Paper or [3]Scissors")
    valid_moves = ["1", "2", "3", "Rock", "Paper", "Scissors"]
    player_move = input(Fore.LIGHTYELLOW_EX + "Your move [1-3]: ")
    if player_move not in valid_moves:
        if computer_score > player_score:
            print(Fore.RED + f"Final score: Player {player_score} - {computer_score} Computer.")
        elif computer_score == player_score:
            print(Fore.YELLOW + f"Final score: Player {player_score} - {computer_score} Computer.")
        else:
            print(Fore.GREEN + f"Final score: Player {player_score} - {computer_score} Computer.")
        raise SystemExit("Invalid input. Try again!")

    if player_move in ["1", "Rock"]:
        player_move = "rock"
    elif player_move in ["2", "Paper"]:
        player_move = "paper"
    else:
        player_move = "scissors"

    computer_random_move = random.randint(1, 3)
    computer_move = ""

    if computer_random_move == 1:
        computer_move = "rock"
    elif computer_random_move == 2:
        computer_move = "paper"
    else:
        computer_move = "scissors"
    print(Fore.BLUE + f"The computer chose {computer_move}.")

    if (player_move == "rock" and computer_move == "scissors") or \
            (player_move == "paper" and computer_move == "rock") or \
            (player_move == "scissors" and computer_move == "paper"):
        print(Fore.GREEN + "You Win!")
        player_score += 1
    elif player_move == computer_move:
        print(Fore.YELLOW + "Draw!")
    else:
        print(Fore.RED + "You Lose!")
        computer_score += 1

    print(f"Player {player_score} - {computer_score} Computer.")

    print(Fore.RESET + "Would you like to play again? (Y/N): ")
    play_again_response = input()

    valid_decision = ["y", "Yes", "YES"]
    if play_again_response.lower() in ('y', 'yes'):
        play_again = True
    else:
        play_again = False
if computer_score > player_score:
    print(Fore.RED + "Computer Wins!")
    print(Fore.RED + f"Final score: Player {player_score} - {computer_score} Computer.")
elif computer_score == player_score:
    print(Fore.YELLOW + "It's a Draw!")
    print(Fore.YELLOW + f"Final score: Player {player_score} - {computer_score} Computer.")
else:
    print(Fore.GREEN + "Player Wins!")
    print(Fore.GREEN + f"Final score: Player {player_score} - {computer_score} Computer.")