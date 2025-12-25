import random
import json
import math
import time

def score(difficulty,attempts):
    username = input("Enter username: ")
    data = {
        "username": username,
        "attempts": attempts,
        "difficulty": difficulty
    }
    with open("Highscore.json", "w") as file:
        json.dump(data, file)
    
def leader_board():
    with open("Highscore.json", "r") as file:
        data = json.load(file)
        print(data)

def Game(chance, Answer):
    list_return = []
    Give_Hint = True
    i = chance
    attempts = 0
    print(f"You have {chance} chanes to guess the correct number.")
    #print(Answer)
    while chance > 0:
        if(Give_Hint):
            if round(i/2) >= chance:
                Hint = input("Want a Hint? Y/N: ")
                if(Hint.upper() == 'Y'):
                    Give_Hint = False
                    print(f"it's bewteen {math.floor(Answer/10) * 10} - {math.ceil(Answer/10) * 10}")

        user = int(input("Enter your guess: "))
        if(user == Answer):
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            list_return.append(attempts)
            list_return.append(True)
            end = time.time()

            list_return.append(end)
            return list_return
        elif(user < Answer):
            print(f"Incorrect! The number is greater than {user}")
            chance -= 1
        else:
            print(f"Incorrect! The number is less than {user}")
            chance -= 1
        attempts += 1
        
    if(chance <= 0):
        print("You have no more chances left.")
        print(f"The answer was {Answer}")
        keep = input("Want to keep playing? Y/N: ")
        if(keep.upper() == 'Y'):
            
            main_menu()
        else: 
            list_return.append(attempts)
            list_return.append(False)
            end = time.time()
            list_return.append(end)
            return list_return
    

def main_menu():
    leaderboard = input("Before starting would you like to see who's on the leaderboard? Y/N: ")
    if(leaderboard.upper() == 'Y'):
        leader_board()
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    
    difficulty = input("Please select the difficulty level: ")
    Answer = random.randint(1,100)
    start = time.time()
    if(difficulty == "1" or difficulty.upper() == "EASY"):
        difficulty_score = "Easy"
        print(f"Great! You have selected the Easy difficulty level.")
        lists = Game(10, Answer)
    elif(difficulty == "2" or difficulty.upper() == "MEDIUM"):
        difficulty_score = "Medium"
        print(f"Great! You have selected the Medium difficulty level.")
        lists = Game(5, Answer)
    else:
        difficulty_score = "Hard"
        print(f"Great! You have selected the Hard difficulty level.")
        lists = Game(3, Answer)
  

    
    if(lists != None):
        if(lists[1]):
            start_end = round(lists[2]-start)

            print(f"Your time to complete the game is {start_end} seconds")
            scoreb = input("Do you wish to be on the scoreboard? (WARNING THIS WOULD REPLACE YOUR OLD SCORE) Y/N: ")
            if(scoreb.upper() == 'Y'):
                score(difficulty_score,lists[0])

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
main_menu()
