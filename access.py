# This program is a simple demonstration of flow control 
# using if else statements in python.

name = input("Enter name: ")
password = input("Enter password: ")

if name == 'Mary':
    print("Hello Mary")
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')
else:
    print("Who are you, stranger?")
