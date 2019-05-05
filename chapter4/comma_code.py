# Practice Project in chapter 4.

spam = ['apples', 'bananas', 'tofu', 'cats']

result_string = ''

if len(spam) > 1:
    for index in range(len(spam) - 1):
        result_string += spam[index] + ', '

    result_string += 'and ' + spam[-1]
elif len(spam) == 1:
    result_string = spam[0]

print(result_string)
