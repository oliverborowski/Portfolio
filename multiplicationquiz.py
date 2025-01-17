#OLIVER BOROWSKI
#Multiplication Quiz
#Initiate
import random
#Functions
wins = 0 #keep tracks of the wins and losses 
def won():
    global wins
    wins = wins + 1
losses = 0
def lost():
    global losses
    losses = losses + 1

#Main
print("Welcome to the Multiplication Quiz")
type = input("Would you like to play with a limit on questions or endless (limit or endless): ")#lets the user devide the amonut of quetions 
type = type.lower()
if type == "limit":
    level = input("What level of questions would you like to answer (easy, medium, or hard): ")
    level = level.lower()
    if level == "easy":#lets the user decide the difficulty
        questions = int(input("How many questions would you like to have in the quiz: "))
        for i in range(questions):
            firstnum = random.randint(1,10)
            secondnum = random.randint(1,10)
            solution = firstnum * secondnum
            print("What is " + str(firstnum) + " x " + str(secondnum) + "?")
            answer = int(input("Your answer: "))
            if solution == answer:
                print("Correct!")
                won()
            else:
                print("Incorrect.")
                lost()
        print("You got " + str(wins) + " out of "+ str(questions) + " questions correct!")
    elif level == "medium":
        questions = int(input("How many questions would you like to have in the quiz: "))
        for i in range(questions):
            firstnum = random.randint(1,20)
            secondnum = random.randint(1,20)
            solution = firstnum * secondnum
            print("What is " + str(firstnum) + " x " + str(secondnum) + "?")
            answer = int(input("Your answer: "))
            if solution == answer:
                print("Correct!")
                won()
            else:
                print("Incorrect.")
                lost()
        print("You got " + str(wins) + " out of "+ str(questions) + " questions correct!")
    elif level == "hard":
        questions = int(input("How many questions would you like to have in the quiz: "))
        for i in range(questions):
            firstnum = random.randint(1,30)
            secondnum = random.randint(1,30)
            solution = firstnum * secondnum
            print("What is " + str(firstnum) + " x " + str(secondnum) + "?")
            answer = int(input("Your answer: "))
            if solution == answer:
                print("Correct!")
                won()
            else:
                print("Incorrect.")
                lost()
        print("You got " + str(wins) + " out of "+ str(questions) + " questions correct!")#shows the correct amount of questoins
    else:
        print("Wrong input")
elif type == "endless":
    while True:
        firstnum = random.randint(1,10)
        secondnum = random.randint(1,10)
        solution = firstnum * secondnum
        print("What is " + str(firstnum) + " x " + str(secondnum) + "?")
        answer = int(input("Your answer: "))
        if solution == answer:
            print("Correct!")
            won()
        else:#if the user does not guess the number
            print("Incorrect.")
            lost()
