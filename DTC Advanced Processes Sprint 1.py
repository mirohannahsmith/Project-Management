##
# Advanced Processes code 

# Author: Miro


# Sprint 1

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

def question_ask(number_1, number_2):
    """ Create function for asking questions.
        Takes:
            Two values from values 3d list
        
        Returns:
            Question for user
    """
    try:
        answer = int(input("What is {} + {}? : ".format(number_1, number_2)))
    except ValueError:
        print("That's not a valid integer. Incorrect.")
        pass
    correct_answer_sum = number_1 + number_2
    if correct_answer_sum == answer:
        print("Correct!")
        pass
    elif answer <= 0:
        print("That number is a negative, incorrect.")
    else:
        print("Incorrect.")


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