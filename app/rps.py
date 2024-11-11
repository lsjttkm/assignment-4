'''
# the "app/rps.py" file (v1)...

from random import choice

VALID_OPTIONS = ["rock", "paper", "scissors"] #refactoring


# USER SELECTION

u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in VALID_OPTIONS:
    print("OOPS, TRY AGAIN")
    exit()


# COMPUTER SELECTION

c = choice(VALID_OPTIONS)
print("COMPUTER CHOICE:", c)


# DETERMINATION OF WINNER

if u == "rock" and c == "rock":
    print("TIE GAME")
elif u == "rock" and c == "paper":
    print("COMPUTER WINS")
elif u == "rock" and c == "scissors":
    print("USER WINS")
elif u == "paper" and c == "rock":
    print("COMPUTER WINS") # OOPS
elif u == "paper" and c == "paper":
    print("TIE GAME")
elif u == "paper" and c == "scissors":
    print("USER WINS") # OOPS
elif u == "scissors" and c == "rock":
    print("COMPUTER WINS")
elif u == "scissors" and c == "paper":
    print("USER WINS")
elif u == "scissors" and c == "scissors":
    print("TIE GAME")

'''
    
# the "app/rps.py" file (v2) ...

from random import choice


VALID_OPTIONS = ["rock", "paper", "scissors"]

USER_WINS_MESSAGE = "USER WINS"
COMPUTER_WINS_MESSAGE = "COMPUTER WINS"
TIE_GAME_MESSAGE = "TIE GAME"


def generate_computer_choice():
    return choice(VALID_OPTIONS)


def determine_outcome(u, c):
    """
    Determines the outcome of a Rock-Paper-Scissors game between a user and the computer.

    Args:
        u (str): The user's choice. Must be one of 'rock', 'paper', or 'scissors'.
        c (str): The computer's choice. Must be one of 'rock', 'paper', or 'scissors'.

    Returns:
        str: The outcome of the game. Returns one of the following:
             - "USER WINS" if the user wins.
             - "COMPUTER WINS" if the computer wins.
             - "TIE GAME" if both selections are the same.

    Raises:
        KeyError: If either `u` or `c` is not one of 'rock', 'paper', or 'scissors'.
    """
    winners = {
        "rock":{
            "rock": TIE_GAME_MESSAGE,
            "paper": COMPUTER_WINS_MESSAGE,
            "scissors": USER_WINS_MESSAGE,
        },
        "paper":{
            "rock": USER_WINS_MESSAGE,
            "paper": TIE_GAME_MESSAGE,
            "scissors": COMPUTER_WINS_MESSAGE,
        },
        "scissors":{
            "rock": COMPUTER_WINS_MESSAGE,
            "paper": USER_WINS_MESSAGE,
            "scissors": TIE_GAME_MESSAGE,
        },
    }
    outcome = winners[u][c]
    return outcome



if __name__ == "__main__": #main conditional; allows us to import code smoothly from this file

    #
    # USER SELECTION
    #

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in VALID_OPTIONS:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = generate_computer_choice()
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    outcome = determine_outcome(u, c)
    print(outcome)