from random import randrange
x = randrange(0, 10)

print("Please guess a number between 0 and 9: ")
guess = int(input())

while True:
    if guess != x:
        if guess > x:
            print("Please guess lower")
        else:
            print("Please guess higher")
        guess = int(input())
        if guess == x:
            print("Correct!")
            break
    else:
        print("You got it the first time!")
        break
