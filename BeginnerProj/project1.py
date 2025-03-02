# Trivia game - You will have a set of questions and answers.
# The user will be asked a question, and they will have to type in the answer.
# The game will keep track of the score and at the end, the user will be given their score out of the total number of questions.

# Plan (think plan before you code) - what do I need to do? How can I break this down into smaller steps that's easier for me to solve? - solve them one by one and combine then together to ultimately come up with the end code.
# 1. Create a list of questions and answers
# 2. Randomly pick the questions
# 3. ask the questions
# 4. check if the answer is correct
# 5. keep track of the score
# 6. at the end, give the score to the user.

import random

# 1. Create a list of questions and answers
questions = { # dictionary
    "What is the keyword to define a function in Python?": "def",
    "Which data type is used to store True or False values?": "boolean",
    "What is the correct file extension for Python files?": ".py",
    "Which symbol is used to comment in Python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What keyword is used to import a module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in Python?": "3"
}

# print(questions['What is the result of 10 // 3 in Python?']) # 3

# 2. Randomly pick the questions
def python_trivia_game(q):
    total_que = 5
    score = 0
    selected_question = random.sample(list(q.keys()), total_que)

    # 3. ask the questions
    for idx, question in enumerate(selected_question):
        # f-String is simply a string that allows you to embed expressions inside of braces
        print(f"{idx + 1}. {question}")
        user_answer = input("Your answer: ").lower().strip() # lower() - convert the string into lowercase, strip() - remove any leading (spaces at the beginning) and trailing (spaces at the end)
        correct_answer = q[question].lower()

        # 4. check if the answer is correct
        if user_answer == correct_answer:
            # 5. keep track of the score
            print("Correct!\n") # \n - move us down to the next line the terminal
            score += 1
        else:
            print(f"Wrong! The correct answer is: {q[question]}.\n")



    return score, total_que


# 6. at the end, give the score to the user.
game_score, total_questions = python_trivia_game(questions)
print(f"Game over! Your score is: {game_score}/{total_questions}")

"""
The highlighted code does the following:

1. `q.keys()` - Gets all the keys (questions) from the dictionary `q`
2. `list()` - Converts the dictionary keys object into a list
3. `random.choice()` - Randomly selects one item from the list

In this context, the code randomly selects one question from the dictionary of questions.
 The `random.choice()` function can only work with sequences (like strings, lists, tuples), which is why the dictionary keys need to be converted to a list first.

For example, if this line runs on the questions dictionary defined above, it might return any one of the questions like "What is the keyword to define a function in Python?" 
or
"Which data type is used to store True or False values?" at random.
"""