import colorama
from colorama import Fore
import random
colorama.init()


rock = "Rock"
paper = "Paper"
scissors = "Scissors"

computer_score = 0
player_score = 0


def play_again():
    print(Fore.RESET + "Would you like to play again? (Y/N): ")
    play_again_response = input()
    accept = ["y", "yes"]
    decline = ["n", "no"]
    if play_again_response.lower() in accept:
        return new_game_1()
    elif play_again_response.lower() in decline:
        print("Would you like to return to the start menu? (Y/N)")
        player_menu_response = input()
        if player_menu_response.lower() in accept:
            return game_start()
        elif player_menu_response.lower() in decline:
            return SystemExit
        else:
            return choose_different_mod()
    else:
        print(Fore.RED + "Invalid input. Try again!")
        return play_again()


def choose_different_mod():
    print("Would you like to return to the start menu? (Y/N):")
    play_again_response = input()
    accept = ["y", "yes"]
    decline = ["n", "no"]
    if play_again_response.lower() in accept:
        return game_start()
    elif play_again_response.lower() in decline:
        return SystemExit
    else:
        print(Fore.RED + "Invalid input. Try again!")
        return choose_different_mod()


def new_game_1():
    computer_score = 0
    player_score = 0
    print(Fore.CYAN + "Now choose: [1]Rock, [2]Paper or [3]Scissors")
    valid_moves = ["1", "2", "3", "Rock", "Paper", "Scissors"]
    player_move = input(Fore.LIGHTYELLOW_EX + "Your move [1-3]: ")
    if player_move not in valid_moves:
        print(Fore.RED + "Invalid input. Try again!")
        return new_game_1()

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

    print(Fore.RESET + "Would you like to play again? (Y/N): ")
    play_again_response = input()

    accept = ["y", "yes"]
    decline = ["n", "no"]
    if play_again_response.lower() in accept:
        return new_game_1()
    elif play_again_response.lower() in decline:
        print("Would you like to return to the start menu? (Y/N):")
        player_menu_response = input()
        if player_menu_response.lower() in accept:
            return game_start()
        elif player_menu_response.lower() in decline:
            return SystemExit
        else:
            return choose_different_mod()
    else:
        print(Fore.RED + "Invalid input. Try again!")
        return play_again()


def new_game_2():
    computer_score = 0
    player_score = 0
    while True:
        print(Fore.CYAN + "Now choose: [1]Rock, [2]Paper or [3]Scissors")
        valid_moves = ["1", "2", "3", "Rock", "Paper", "Scissors"]
        player_move = input(Fore.LIGHTYELLOW_EX + "Your move [1-3]: ")
        if player_move not in valid_moves:
            print(Fore.RED + "Invalid input. Try again!")
            continue
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
        print(Fore.BLUE + f"Current score: Player {player_score} - {computer_score} Computer.")
        if computer_score + player_score == 3 or player_score == 2 or computer_score == 2:
            if computer_score > player_score or computer_score == 2:
                print(Fore.RED + "Computer Wins!")
                print(Fore.RED + f"Final score: Player {player_score} - {computer_score} Computer.")
            elif computer_score == player_score:
                print(Fore.YELLOW + "It's a Draw!")
                print(Fore.YELLOW + f"Final score: Player {player_score} - {computer_score} Computer.")
            else:
                print(Fore.GREEN + "Player Wins!")
                print(Fore.GREEN + f"Final score: Player {player_score} - {computer_score} Computer.")

            accept = ["y", "yes"]
            decline = ["n", "no"]
            flag = True
            while flag:
                print(Fore.RESET + "Would you like to play again? (Y/N):")
                play_again_response = input()
                if play_again_response.lower() in accept:
                    return new_game_2()
                elif play_again_response.lower() in decline:
                    print("Would you like to return to the start menu? (Y/N):")
                    player_menu_response = input()
                    if player_menu_response.lower() in accept:
                        return game_start()
                    elif player_menu_response.lower() in decline:
                        return SystemExit
                    else:
                        print(Fore.RED + "Invalid input. Try again!")
                        continue
                else:
                    print(Fore.RED + "Invalid input. Try again!")
                    continue


def new_game_3():
    computer_score = 0
    player_score = 0
    while True:
        print(Fore.CYAN + "Now choose: [1]Rock, [2]Paper or [3]Scissors")
        valid_moves = ["1", "2", "3", "Rock", "Paper", "Scissors"]
        player_move = input(Fore.LIGHTYELLOW_EX + "Your move [1-3]: ")
        if player_move not in valid_moves:
            print(Fore.RED + "Invalid input. Try again!")
            continue

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

        accept = ["y", "yes"]
        decline = ["n", "no"]
        flag = True
        while flag:
            print(Fore.RESET + "Would you like to stop? (Y/N): ")
            play_again_response = input()
            if play_again_response.lower() in accept:
                if computer_score > player_score:
                    print(Fore.RED + "Computer Wins!")
                    print(Fore.RED + f"Final score: Player {player_score} - {computer_score} Computer.")
                elif computer_score == player_score:
                    print(Fore.YELLOW + "It's a Draw!")
                    print(Fore.YELLOW + f"Final score: Player {player_score} - {computer_score} Computer.")
                else:
                    print(Fore.GREEN + "Player Wins!")
                    print(Fore.GREEN + f"Final score: Player {player_score} - {computer_score} Computer.")
                print("Would you like to return to the start menu? (Y/N):")
                player_menu_response = input()
                if player_menu_response.lower() in accept:
                    return game_start()
                elif player_menu_response.lower() in decline:
                    return SystemExit
                else:
                    print(Fore.RED + "Invalid input. Try again!")
                    continue
            elif play_again_response.lower() in decline:
                flag = False
            else:
                print(Fore.RED + "Invalid input. Try again!")
                continue


def game_start():
    print(Fore.GREEN + "Let the 'Rock, Paper or Scissors' game begin!!")
    print("Choose a game mode:")
    print("1 - Single game.")
    print("2 - Best of Three.")
    print("3 - Infinite")
    valid_game_modes = ["1", "2", "3"]
    game_mode = input(Fore.BLUE + "Game Mode: ")
    while game_mode not in valid_game_modes:
        print("Invalid input. Choose again!")
        game_mode = input(Fore.BLUE + "Game Mode: ")
        if game_mode in valid_game_modes:
            break
    if game_mode == "1":
        return new_game_1()
    elif game_mode == "2":
        return new_game_2()
    else:
        return new_game_3()


game_start()

