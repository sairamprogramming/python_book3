# Program is demonstration on if - elif - else statements.
# Also this program shows that the order of the elif 
# statment matters.

name = input('Enter name: ')
age = int(input("Enter age: "))

if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100: # This is a bug since any number > 2000 is also > 100.
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 2000:    # This line will never be executed 
    print('You are not Alice, grannie.')
