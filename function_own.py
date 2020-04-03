def hello(): # defining this new function
    print('Hello!') #body of the function
    print('Hello!')
    print('Hi there!')

hello() # Calling 2 times. This is to make code shorter, not to type print 3 times
hello()

def hello(name):
    print('Hello ' + name)

hello('Alice')
hello('Bob')

def plusOne(number):
    return (number+1)

newNumber = plusOne(5)
print(newNumber)

print('Hello', end = '')
print('World')

print('cat', 'dog', 'mouse', sep = 'ABC')


'''def spam():
    eggs = 31337

spam()
print(eggs) # This is error, it cannot reach local variable eggs, and there is no global variable called eggs
'''