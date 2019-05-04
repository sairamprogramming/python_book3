# This program is pratice project in the chapter 3

# In this program we find create a function that prints the collatz
# sequence of a given number.

def main():
    # Flag if the input is valid.
    correct_input = False

    # Input Validation.
    try:
        number_input = int(input('Enter a number: '))
        correct_input = True
    except:
        print('Error: Input is invalid!')
    
    # Calling the collatz() function if call is not raised.
    if correct_input:
        collatz(number_input)

# Function prints the collatz sequence for a given argument.
def collatz(number):
    
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
        print(number)

# Calling the main function.
main()