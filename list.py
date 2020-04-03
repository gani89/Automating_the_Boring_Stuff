for i in range(4):
    print (i)

for i in [0, 1, 2, 3]:
    print (i)

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in list is: ' + supplies[i])

import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam) # this creates brand new list
cheese[1] = 'Hello'

print(spam)
print(cheese)
