import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

print("Choose [1]Rock, [2]Paper, or [3]Scissors")
valid_moves = ["1", "2", "3", "Rock", "Paper", "Scissors"]
player_move = input("Your move [1-3]: ")
if player_move not in valid_moves:
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
print(f"The computer chose {computer_move}.")

if player_move == "rock" and computer_move == "scissors":
    print("You win!")
elif player_move == "paper" and computer_move == "rock":
    print("You win!")
elif player_move == "scissors" and computer_move == "paper":
    print("You win!")
elif player_move == computer_move:
    print("Draw!")
else:
    print("You lose!")




