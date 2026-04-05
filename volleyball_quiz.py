# a volleyball quiz on common rules (CLI)
# started: April 4, 2026 (night)
# finished: April 5, 2026 (arvo)
import random
import time

# dictionary of questions and answers
questions = {
    "How many players are on the court per team in volleyball?": "6",
    "How many touches is a team allowed before sending the ball over?": "3",
    "What is it called when a serve results directly in a point?": "ace",
    "What is the term for hitting the ball over the net with force?": "spike",
    "What position usually sets up the ball for attackers?": "setter",
    "What is it called when a player prevents the ball from hitting the ground after a spike?": "dig",
    "What is the defensive move at the net to stop a spike?": "block",
    "What is the rotation direction in volleyball?": "clockwise",
    "How many points are needed to win a standard set (not final set)?": "25",
    "What is the name of the player who specializes in defense and wears a different jersey?": "libero"
}

correct = 0
incorrect = 0

# explain the game
print("Welcome to the VOLLEYBALL QUIZ!")
time.sleep(3)
print("Your goal is to answer 5 questions right!")
time.sleep(3)
print("If you answer more than 3 questions wrong, you lose!")
time.sleep(3)
print("Good luck, and have fun!")
time.sleep(3)

# main game loop
while True:
    # list(questions) extracts the keys in the dictionary, and stores it in a list
    list_of_questions = list(questions)

    # pick a random question
    question = random.choice(list_of_questions)

    # ask them a question; give time to read
    print(question)
    time.sleep(3)

    # ask the user to answer
    answer = input(" ").strip().lower()

    # if they get it right
    if answer == questions[question]:
        print("Correct! \n")
        time.sleep(2)

        # update and print new stats
        correct += 1
        # 5 right answers results in a win
        if correct == 5:
            print("Congratulations! You have got 5 questions right!")
            time.sleep(3)

            print("You win!")
            time.sleep(2)

            break

        print(f"Correct: {correct}")
        print(f"Incorrect: {incorrect}")
        time.sleep(3)

    # if they get it wrong
    else:
        print("Incorrect... \n")
        time.sleep(2)

        # update and print new stats
        incorrect += 1
        # more than 3 wrong answers results in game over
        if incorrect > 3:
            print("Oh no! You have got more than 3 questions wrong!")
            time.sleep(3)

            print("Game over!")
            time.sleep(2)

            break

        else:
            print(f"Correct: {correct}")
            print(f"Incorrect: {incorrect}")
            time.sleep(3)

    # remove that random question from the dictionary
    questions.pop(question)
