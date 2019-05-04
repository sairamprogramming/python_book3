# Program demonstrates that the same variable name can be used
# for a global variable and local variable.

# This is bad practice and should be avoided.

def spam():
    eggs = 'spam local'
    print(eggs)             # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs)             # prints 'bacon local'
    spam()
    print(eggs)             # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs)                 # prints 'global'    