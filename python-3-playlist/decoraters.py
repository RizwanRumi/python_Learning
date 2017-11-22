#extend the behaviour without modifying function itself.

def ques_code(func):

    def wrapper_ques():
        print('*note: you must have to answer*')

        func() # --> question()

        print('*Please think twice before answer*')
    return wrapper_ques

@ques_code
def question():
    print("Are you filling occured in this question?")

@ques_code
def answer():
    print("Give the correct answer")

question()
print('-------------------')
answer()
