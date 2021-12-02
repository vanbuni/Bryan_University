import random
attempts = 0
hiddenNumber = random.randint(1,10)

while True:
    print("Guess a number between 1 and 10. To quit game, type quit")
    userGuess = input()
    quitGame = str(userGuess)
    if quitGame == 'quit':
        print("You have quit the game")
        break
    elif not userGuess.isdigit():
        print("Only numbers allowed")
    else:
        userGuess = int(userGuess)
        attempts +=1
        if userGuess > 10 or userGuess <=0:
            attempts -=1
            print("Only numbers between 1 and 10! \n")
        elif userGuess < hiddenNumber and userGuess > 0:
            print("Nope! Try a higher number! \n")
        elif userGuess > hiddenNumber and userGuess <= 10:
            print("Nope! Try a lower number! \n")
        if userGuess == hiddenNumber:
            attempts = str(attempts)
            print("You win! It only took you " + attempts + " attempts.")
            break
