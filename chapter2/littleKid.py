# Simple program.

name = input("Enter name: ")
age = int(input("Enter age: "))

if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')
