# Program to demonstrate the use of global statement in a function.

def spam():
    global eggs         # This statement tells python that now eggs in this function refers to the eggs in global variable.
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)