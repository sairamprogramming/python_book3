# This program is a demonstration on 'Truthy' and 'Falsey' values.
# False values in python {0, 0.0, ''}

name = ''
# Here we use the truthy/ falsey to check the condtion of the loop.
while not name:
    print("Enter your name:")
    name = input()
print('How many guest will you have?')
numOfGuests = int(input())
if numOfGuests:
    print('Be sure to have enough rom for all your guests.')
print('Done')
