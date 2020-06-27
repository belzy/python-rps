import sys

def main():

    ### Necessary variables
    # welcome_message
    # historical_data_message
    # quit_message
    # win_message
    # loss_message
    # tie_message

    # wins
    # ties
    # losses

    # choice_options

    # computer_choice
    # user_choice

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

    import random

    score = {
        "wins": 0,
        "ties": 0,
        "losses": 0
    }

    welcome_message = "Welcome to Rock, Paper, Scissors!"
    historical_data_message = "Wins: %s, Ties: %s, Losses: %s"
    input_message = "[1] rock   [2] paper   [3] scissors    [9] quit\n"
    quit_message = "Thanks for playing Rock, Paper, Scissors"
    win_message = "Congratulations, you won!"
    loss_message = "Sorry, you lost!"
    tie_message = "It was a tie"

    historical_data = { #TODO: Will need a function for loading historical data
        "wins": 0,
        "ties": 0,
        "losses": 0
    } 

    score["wins"] = historical_data["wins"]
    score["ties"] = historical_data["ties"]
    score["losses"] = historical_data["losses"]

    choice_options = {
        1: "rock",
        2: "paper",
        3: "scissors",
        9: "quit"
    }

    computer_choice = random.randint(1, 3)
    user_choice = None

    ### 1. Display welcome message
    def show_welcome_message(message="Hello world!"):
        print(message)

    ### 2. Load historical data and populate variables with data
    def get_historical_data():

        text_file = open("history.txt", "r")
        text_data = text_file.read().split(",")
        text_file.close()

        return {
            "wins": int(text_data[0]),
            "ties": int(text_data[1]),
            "losses": int(text_data[2])
        }

    ### 3. Display historical data message with historical data
    def show_historical_data_message(message, rps_data={"wins": 0, "ties": 0, "losses": 0}):
        print(message % (rps_data["wins"], rps_data["ties"], rps_data["losses"]))

    ### 4. Prompt user to make a choice between rock, paper, scissors, or quit
    def get_user_choice(message="Your Input"):
        choice = input(message)
        return choice_options[int(choice)]

    ### 4.1 If quit, update text file with current wins, ties, losses data and exit game
    def quit_game(wins, ties, losses):
        text_file = open("history.txt", "w")
        text_file.write(str(wins) + "," + str(ties) + "," + str(losses))
        text_file.close()

    return 0

main()