#Guessing Number Game

import random
import time
import os


level_hard_attempts = 5
level_easy_attempts = 10

#Computer --> taking as an answer variable...!
answer = random.randint(1, 50)


#Functions
def game():
    level = input('\n\nChoose level of diffculty...Type "Hard" or "Easy": ')
    if level == "Hard" or level == "hard":
        time.sleep(2)
        print("\nEntering level Hard...\n\nLet me think of a number between 1 to 50! --> 🤔\n")
        time.sleep(3)
        attempts = 5
        print("\n    Okay I guessed a number 😁    ")
        while True:
            print("\nYou have", attempts, "attemps remaining to guess the number...!")
            guess = int(input("Make a guess: "))
            attempts -= 1
            if attempts == 0:
                print("\nYou loose! The correct number was", answer)
                print("\n\n")
                time.sleep(5)
                return start()
                
            elif guess == answer:
                print("\nCorrect! You guessed the number in", level_hard_attempts - attempts, "attempts.")
                print("\n\n")
                time.sleep(5)
                return start()
            
            if guess > answer:
                print("Your guess is too high!\nGuess again!")
            elif guess < answer:
                print("Your guess is too low!\nGuess again!")

    elif level == "Easy" or level == "easy":
        time.sleep(2)
        print("\nEntering level Easy...\n\nLet me think of a number between 1 to 50! --> 🤔\n")
        time.sleep(3)
        attempts = 10
        print("\n    Okay I guessed a number 😁    ")
        while True:
            print("\nYou have", attempts, "attemps remaining to guess the number...!")
            guess = int(input("Make a guess: "))
            attempts -= 1
            if attempts == 0:
                print("\nYou loose! The correct number was", answer)
                print("\n\n")
                time.sleep(5)
                return start()
                
            elif guess == answer:
                print("\nCorrect! You guessed the number in", level_easy_attempts - attempts, "attempts.")
                print("\n\n")
                time.sleep(5)
                return start()
            
            if guess > answer:
                print("Your guess is too high!\nGuess again!")
            elif guess < answer:
                print("Your guess is too low!\nGuess again!")

    elif level == "Q" or level == "q":
        sure = input("Are you sure? (Yes/No) --> ")
        if sure == "Yes" or sure == "yes":
            print("Okay Sure...!\n\n")
            time.sleep(2)
            return start()
        elif sure == "No" or sure == "no":
            print("Okay fine...!\n")
            time.sleep(2)
            return game()
        else:
            print("Invalid Command!\n")
            time.sleep(3)
            return game()
    else:
            print("Invalid Command!\n")
            time.sleep(3)
            return game()



def start():
    while True:
        asking = input('\nEnter "P" to play the game\nEnter "Q" to close the game\nEnter your choice: --> ')
        if asking == "P" or asking == "p":
            print("Okay, ready!")
            print("Note: For getting back from game, just enter 'Q' and game will over and you'll come out of the game!\n\n")
            time.sleep(3)
            os.system("cls")
            print("\tGame Starts...")
            while True:
                game()
        elif asking == "Q" or asking == "q":
            sure = input("Are you sure? (Yes/No) --> ")
            if sure == "Yes" or sure == "yes":
                print("Okay, as you wish!\n")
                time.sleep(3)
                exit()
            elif sure == "no" or sure == "No":
                print("Okay, so you want to get back...😅\n")
                time.sleep(2)
            else:
                print("Invalid Command!\n")
                time.sleep(2)
        else:
            print("Invalid Command!\n")
            time.sleep(2)



#Starting Game........!

print("\tGuessing Number\n")
while True:
    start()