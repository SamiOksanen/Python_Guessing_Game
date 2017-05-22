from random import randrange
x = randrange(0, 10)

guess = int(input("Please guess a number between 0 and 9: "))

while True:
    if guess != x:
        if guess > x:
            guess = int(input("Please guess lower: "))
        else:
            guess = int(input("Please guess higher: "))
        if guess == x:
            print("Correct!")
            break
    else:
        print("You got it the first time!")
        break
