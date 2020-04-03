# This is a guess the number game

import random # to use randint function

print('Hello. What is your name?')
name = input()

print('Hello ' + name + '. I am thinking a number between 1 and 20')

secretNumber = random.randint(1, 20)

a = 0

while True:
    print ('Take a guess')
    guess = int(input())
    a=a+1
    if a>=6:
        print('You took too many attempts. The random number was ' + str(secretNumber))
        break
    elif guess > secretNumber:
        print('Your guess is too high')
    elif guess < secretNumber:
        print ('Your guess is too low')
    else:
        print('Good job, ' + name + '!')
        print('You guessed it in ' + str(a) + ' attempts')
        break