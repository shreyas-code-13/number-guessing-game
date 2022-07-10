import random
randNumber = random.randint(1, 100)
print(randNumber)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses+=1
    if(userGuess == randNumber):
        print("****** Hooray! You guessed it right! ******")
    elif(userGuess<randNumber):
        print("Higher Number Please.")
    elif(userGuess>randNumber):
        print("Lower Numer Please.")

print(f"You guessed the number in {guesses} attempts.")
with open("hiscore.txt") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("_____NEW HIGH SCORE_____")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))