# Program on demonstration of global and local variable.

def spam():
    global eggs
    eggs = 'spam'       # this is global scope eggs.

def bacon():
    eggs = 'bacon'      # this is local scope eggs.

def ham():
    print(eggs)         # this is global scope eggs.

eggs = 42               # this is global scope eggs.
spam()
print(eggs)