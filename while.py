'''spam = 0

while spam < 5:
    print('Hello World!')
    spam = spam+1

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()

print('Thank you!')

#name = ''

while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

'''

spam = 0

while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print ('The spam value is ' + str(spam))