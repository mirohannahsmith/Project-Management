"""This file asks the user maths questions in a game."""
# Advanced Processes code

# Author: Miro

# Import random used for later
from random import randint

# Add 3d list full of integers for questions of varying difficulties
# There are 10 difficulty levels, each getting harder than the last.
VALUES = [[1, 2, 3, 4, 5, 10],  # Difficulty level 1
          [6, 7, 8, 9, 11, 12],  # Difficulty level 2
          [10, 20, 40, 60, 80, 100],  # Difficulty level 3
          [13, 14, 17, 21, 23, 25],  # Difficulty level 4
          [34, 46, 58, 41, 76, 88],  # Difficulty level 5
          [101, 134, 147, 176, 188, 231],  # Difficulty level 6
          [171, 257, 387, 478, 272, 363],  # Difficulty level 7
          [512, 672, 843, 932, 476, 1035],  # Difficulty level 8
          ]

# Define scoreboard for points variable
global points_score
points_score = 0

# Define formatting functions


# Define function for printing gaps
def gaps_print(gaps_number):
    """Print new lines when needed.

    Takes parameters of a number and prints that many.
    """
    for i in range(gaps_number):
        print("")
    return gaps_number


# Define function for printing lines
def line_print(line_value):
    """Print lines needed for formatting.

    Takes parameters of a number and prints that many lines.
    """
    print("-" * line_value)
    return line_value


# Define function for exiting code when user loses.
def exit_code():
    """End code.

    Exits code when user gets answer incorrect.
    """
    gaps_print(2)
    line_print(40)
    print("You have lost the game, sorry.")
    line_print(40)
    # Exits code and ends the game
    exit()


# Set variable for bonus points
BONUS_POINTS = 10000


# Print ending message for winners
def winning_message():
    """Print the message when the user wins."""
    gaps_print(1)
    global points_score
    # Adds bonus points to points score
    points_score += BONUS_POINTS
    print("Congratulations, you have won the game!")
    # Prints bonus point amount
    print("You win an extra {} points!".format(BONUS_POINTS))
    # Prints final score with bonus points
    print("This brings your final total points to {}".format(points_score))
    line_print(55)
    # Exits code and ends the game
    exit()


# Variable makes message of continue instructions only print once
repeat_continue_instructions = True


# Set variable which makes continue message not print after question 8
continue_after_q8 = 0


def user_continue():
    """End code.

    Exits code when user wishes to stick to points.
    """
    global continue_after_q8
    continue_after_q8 += 1
    # After question 8 display the winning message instead of continuing
    if continue_after_q8 == 8:
        winning_message()
    gaps_print(1)
    global repeat_continue_instructions
    # Displays instructions only once
    if repeat_continue_instructions is True:
        line_print(60)
        print("You are now given the chance to continue.")
        print("If you do, you will double your points.")
        print("If you fail, you'll lose the game and all points.")
        print("You can leave now and end the game with your current points.")
        repeat_continue_instructions = False
    gaps_print(1)
    # Gives user instructions on what to enter
    print("Enter Y to continue or N to end the game.")
    gaps_print(1)
    # Set loop for asking user to continue
    user_continue_loop = False
    while user_continue_loop is not True:
        # Ask user if they want to continue
        continue_answer = input("Do you want to continue? : ")
        continue_answer = continue_answer.lower()
        # If user wants to continue, do so
        if continue_answer == "y":
            user_continue_loop = True
        # If user doesn't want to continue, end game.
        elif continue_answer == "n":
            line_print(25)
            # Display final score
            print("Your final score: {}".format(points_score))
            print("Thank you for playing!")
            line_print(25)
            exit()
        else:
            # If user enters invalid, repeat question
            gaps_print(1)
            print("Please enter either 'Y' or 'N'.")
            gaps_print(1)


# Define function used for asking the question
def question_ask(number_1, number_2):
    """Asks users the maths questions.

    Takes:
        Two values from values 3d list
    """
    gaps_print(1)
    line_print(25)
    try:
        # Ask question, taking values as random numbers
        answer = int(input("What is {} + {}? : ".format(number_1, number_2)))
    # If user enters a non-integer, automatic loss
    except ValueError:
        gaps_print(1)
        print("That's not a valid integer. Incorrect.")
        line_print(25)
        exit_code()
    # Calculate correct answer
    correct_answer_sum = number_1 + number_2
    if correct_answer_sum == answer:
        # If user is correct, continue
        gaps_print(1)
        print("Correct!")
        gaps_print(1)
        global points_score
        # For first question, only give them 10 points
        if points_score == 0:
            points_score += 10
        # Afterwards, double points
        else:
            points_score *= 2
        print("Your score: {}".format(points_score))
        line_print(25)
        user_continue()
    # If user enters a negative, automatic loss
    elif answer < 0:
        gaps_print(1)
        print("That number is a negative, incorrect.")
        line_print(25)
        exit_code()
    # If user enters the wrong answer, loss
    else:
        gaps_print(1)
        print("Incorrect.")
        line_print(25)
        exit_code()


# Print welcome message for user
line_print(30)
print("Welcome to the Maths Game.")
print("You will be asked a series of")
print("maths questions, each question")
print("harder than the one before it.")
line_print(30)
print("Get all 8 questions correct,")
print("and you will win.")
print("Yet if you get any wrong,")
print("you will lose the game.")

# Print questions that take random parameters from list

# Set variable for changing difficulty level
difficulty_swap = 0
# Loop to go through all 8 difficulty levels
for i in range(8):
    question_ask(VALUES[difficulty_swap][randint(0, 5)],
                 VALUES[difficulty_swap][randint(0, 5)])
    # Changes difficulty level every loop
    difficulty_swap += 1
