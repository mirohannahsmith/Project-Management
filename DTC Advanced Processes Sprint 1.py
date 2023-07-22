##
# Advanced Processes code 

# Author: Miro

# Import random used for later
from random import randint

# Add 3d list full of integers for questions of varying difficulties
# Each line has 6 numbers which will be randomly added together to make the questions
# There are 10 difficulty levels, each getting harder than the last.
VALUES = [[1, 2, 3, 4, 5, 10], # Difficulty level 1
          [6, 7, 8, 9, 11, 12], # Difficulty level 2
          [10, 20, 40, 60, 80, 100], # Difficulty level 3
          [13, 14, 17, 21, 23, 25], # Difficulty level 4
          [34, 46, 58, 41, 76, 88], # Difficulty level 5
          [101, 134, 147, 176, 188, 231], # Difficulty level 6
          [171, 257, 387, 478, 272, 363], # Difficulty level 7
          [512, 672, 843, 932, 476, 1035], # Difficulty level 8
]

# Define scoreboard for points variable
global points_score
points_score = 0

# Define formatting functions

def gaps_print(gaps_number):
    """This function prints new lines when needed;
    Takes parameters of a number and prints that many.
    """
    for i in range(gaps_number):
        print("")
    return gaps_number


def line_print(line_value):
    """This function prints lines needed for formatting;
    Takes parameters of a number and prints that many lines.
    """
    print("-" * line_value)
    return line_value


def exit_code():
    """This function is used for ending code;
    Exits code when user gets answer incorrect.
    """
    gaps_print(2)
    line_print(40)
    print("You have lost the game, sorry.")
    line_print(40)
    exit()


def user_continue():
    """This function is used for ending code;
    Exits code when user wishes to stick to points.
    """
    line_print(60)
    print("You are now given the chance to continue.")
    print("If you do, you will double your points.")
    print("If you fail, you'll lose the game and all points.")
    print("You can leave now and end the game with your current points.")
    gaps_print(1)
    print("Enter Y to continue or N to end the game.")
    gaps_print(1)
    user_continue_loop = False
    while user_continue_loop is not True:
        continue_answer = input("Do you want to continue? : ")
        if continue_answer == "Y" or "y":
            user_continue_loop = True
        elif continue_answer == "N" or "n":
            line_print(20)
            print("Your final score: {}".format(points_score))
            print("Thank you for playing.")
            line_print(20)
            exit()
        else:
            print("Please enter either 'Y' or 'N'.")


user_continue()

def question_ask(number_1, number_2):
    """ Create function for asking questions.
        Takes:
            Two values from values 3d list
        
        Returns:
            Question for user
    """
    gaps_print(1)
    line_print(25)
    try:
        answer = int(input("What is {} + {}? : ".format(number_1, number_2)))
    except ValueError:
        gaps_print(1)
        print("That's not a valid integer. Incorrect.")
        line_print(25)
        exit_code()
    correct_answer_sum = number_1 + number_2
    if correct_answer_sum == answer:
        gaps_print(1)
        print("Correct!")
        gaps_print(1)
        global points_score
        points_score += 10
        print("Your score: {}".format(points_score))
        line_print(25)
    elif answer < 0:
        gaps_print(1)
        print("That number is a negative, incorrect.")
        line_print(25)
        exit_code()
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

#Ask difficulty level one question
question_ask(VALUES[0][randint(0, 5)], VALUES[0][randint(0, 5)])

#Ask difficulty level two question
question_ask(VALUES[1][randint(0, 5)], VALUES[1][randint(0, 5)])

#Ask difficulty level three question
question_ask(VALUES[2][randint(0, 5)], VALUES[2][randint(0, 5)])

#Ask difficulty level four question
question_ask(VALUES[3][randint(0, 5)], VALUES[3][randint(0, 5)])

#Ask difficulty level five question
question_ask(VALUES[4][randint(0, 5)], VALUES[4][randint(0, 5)])

#Ask difficulty level six question
question_ask(VALUES[5][randint(0, 5)], VALUES[5][randint(0, 5)])

#Ask difficulty level seven question
question_ask(VALUES[6][randint(0, 5)], VALUES[6][randint(0, 5)])

#Ask difficulty level eight question
question_ask(VALUES[7][randint(0, 5)], VALUES[7][randint(0, 5)])


# Set variable for bonus points
bonus_points = 10000
points_score += bonus_points

# Print ending message for winners
gaps_print(1)
line_print(55)
print("Congratulations, you have won the game!")
print("Just for winning, you can have an extra {} points!".format(bonus_points))
print("This brings your final total points to {}".format(points_score))
line_print(55)