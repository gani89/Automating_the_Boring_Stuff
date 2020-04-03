'''def div42by(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError: # We can also have except without any specific error, in that case it catches all
        print('Error: You tried to divide by zero.')

print(div42by(2))
print(div42by(7))
print(div42by(0)) # Error here
print(div42by(1))
'''

print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats')
    else:
        print('That is not that many')
except ValueError:
    print('You did not enter a number.')

