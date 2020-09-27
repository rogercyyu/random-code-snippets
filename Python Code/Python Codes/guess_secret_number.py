# guessing game
import random
secretNumber = random.randint(1,100)
print('I am thinking of a random number between 1 to 100.')

# ask the player to guess 16 times.
for guessesTaken in range(1,17):
    print('Take a guess.');
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This conditions is the correct guess!

if guess == secretNumber:
    print('Good job! You guess my number in ' +str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
