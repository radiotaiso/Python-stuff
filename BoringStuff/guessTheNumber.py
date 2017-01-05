import random
secretNumber = random.randint(1,20)
print "Guess the number, it's between 1 and 20 just because"
print "you only get 6 chances"
#You only get 6 chances biatch
for guesesTaken in range(1,7):
    print "Take a guess.."
    guess=int(input())

    if guess < secretNumber:
        print "Too low!"
    elif guess > secretNumber:
        print "Too high dude!"
    else:
        break #This means you hit the right number
if guess == secretNumber:
    print "Awesome, you guessed in "+str(guesesTaken)+" guesses!"
else:
    print "nope you suck, the number I was thinking was "+ str(secretNumber)+"...dunce"
