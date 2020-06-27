import sys
import random


def main():

    ### Necessary variables
    
    # Constants
    welcome_message = "Welcome to Rock, Paper, Scissors!"
    historical_data_message = "Wins: %s, Ties: %s, Losses: %s"
    input_message = "[1] rock   [2] paper   [3] scissors   [4] Score   [9] quit\n"
    quit_message = "Thanks for playing Rock, Paper, Scissors"
    win_message = "Congratulations, you won!"
    loss_message = "Sorry, you lost!"
    tie_message = "It was a tie"

    choice_options = {
        1: "rock",
        2: "paper",
        3: "scissors",
        4: "score",
        9: "quit"
    }

    # Variables
    historical_data = {
        "wins": 0,
        "ties": 0,
        "losses": 0
    }

    score = {
        "wins": 0,
        "ties": 0,
        "losses": 0
    }

    computer_choice = random.randint(1, 3)
    user_choice = None

    ### Procedures
    # 1. Display welcome_message
    # 2. Load historical data and populate variables with data
    # 3. Display historical data message with historical data
    # 4. Prompt user to make a choice between rock, paper, scissors, or quit
    #   a. If quit, update text file with current wins, ties, losses data and exit game
    #   b. If not quit, move to step 5
    # 5. Computer makes a choice between rock, paper, and scissors
    # 6. Compare user choice and computer choice
    # 7. Display message based on result of comparison
    # 8. Update wins, ties, and losses
    # 9. Return to step 4

    # 1. Display welcome message
    def show_welcome_message(message="Hello world!"):
        print(message)

    # 2. Load historical data and populate variables with data
    def get_historical_data():

        text_file = open("history.txt", "r")
        text_data = text_file.read().split(",")
        text_file.close()

        return {
            "wins": int(text_data[0]),
            "ties": int(text_data[1]),
            "losses": int(text_data[2])
        }

    # 3. Display historical data message with historical data
    def show_historical_data_message(message=historical_data_message, rps_data={"wins": 0, "ties": 0, "losses": 0}):
        print(message %
              (rps_data["wins"], rps_data["ties"], rps_data["losses"]))

    # 4. Prompt user to make a choice between rock, paper, scissors, or quit
    def get_user_choice(message=input_message):
        choice = input(message)
        return choice_options[int(choice)]

    # 4.1 If quit, update text file with current wins, ties, losses data and exit game
    def quit_game(wins, ties, losses, message=quit_message):

        display_current_score(wins, ties, losses)
        print(f'{message}')

        text_file = open("history.txt", "w")
        text_file.write(str(wins) + "," + str(ties) + "," + str(losses))
        text_file.close()

    # 5. Display the current score
    def display_current_score(wins, ties, losses):
        print(f'Current Score:\nWins - {wins}\nTies - {ties}\nLosses - {losses}')

    # 6. Compare user choice and computer choice
    def compare_choices_and_get_result(user, computer):
        if user == computer:
            return "tie"
        elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
            return "win"
        else:
            return "loss"

    # 7. Display message based on result of comparision
    # 8. Update wins, ties, losses
    def display_result_message_and_update_score(result, user, computer):

        print(f'Your choice: {user}\nComputer choice: {computer}')

        if result == "tie":
            print(tie_message)
            score["ties"] += 1
        elif result == "win":
            print(win_message)
            score["wins"] += 1
        elif result == "loss":
            print(loss_message)
            score["losses"] += 1
            

    ### Start of game
    historical_data = get_historical_data()
    score = historical_data
    show_welcome_message(welcome_message)
    
    ### Game loop
    while user_choice != "quit":

        # Player choices
        user_choice = get_user_choice(input_message)
        computer_choice = choice_options[random.randint(1, 3)]

        # Display score
        if user_choice == 'score':
            display_current_score(score['wins'], score['ties'], score['losses'])
            continue

        # Compare choices
        result = compare_choices_and_get_result(user_choice, computer_choice)
        display_result_message_and_update_score(result, user_choice, computer_choice)

    ### Quit game if user exits game loop
    quit_game(score["wins"], score["ties"], score["losses"])


    return 0


main()
