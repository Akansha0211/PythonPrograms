# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

score = input("Enter Score: ")  # returns a string
score_grade = float(score)  #converts a string output to float value
if (score_grade > 0.0 and score_grade < 1.0):    # we directly use 'or' , 'and' inside expression
    try:        # try-except block to catch traceback
        if (score_grade >= 0.9):
            print('A')
        elif (score_grade >= 0.8):
            print('B')
        elif (score_grade >= 0.7):
            print('C')
        elif (score_grade >= 0.6):
            print('D')
        elif (score_grade < 0.6):
            print('F')
    except:
        score_grade = 2;
else:print("Not a valid number")   # if neither inside try or except block



