import pprint
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

for k in myCat.keys():
    print(k)

for v in myCat.values():
    print(v)

for k, v in myCat.items():
    print(k, v)

myCat.setdefault('age', '8')
print(myCat)
pprint.pprint(myCat)

# program that counts the number of occurrences of each letter in a string

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0) # key part of dictionary is a letter, and initial value of it is zero.
                                   # we are creating/modifying dictionary count
    count[character] = count[character] + 1 # after first appearance, value becomes 1, and increments every time

pprint.pprint(count)