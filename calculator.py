"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

from functools import reduce
while True:
    operations =['+', '-', '*', '/', 'square', 'cube', 'pow', 'mod']
    equation = input('Enter equation: ')
    
    eq = equation.split(' ')

    if "q" in eq:
        print("Exiting")
        break

    nums_only= eq[1:]
    nums_ = []

    for num in nums_only:
        if num.isdigit():
            nums_.append(int(num))
    if len(nums_)!= len(nums_only):
        print("Try again using only digits following the operator.")
        continue

    if eq[0] not in operations:
        print("Enter a valid operation.")
        continue
    
    two_digit_operations = ['+', '-', '*', '/', 'pow', 'mod']
    one_digit_operations = ['square', 'cube']

    if eq[0] in two_digit_operations and len(eq) < 3:
        print("Enter at least two numbers to perform this operation")
        continue

    elif eq[0] in one_digit_operations and len(eq) > 2:
        print("Enter only one number for this operation.")
        continue


    elif eq[0] == '+':

        answer = add(nums_)

    elif eq[0] == '-':
        answer = subtract(nums_)
    
    elif eq[0] == '*':
        answer = multiply(nums_)

    elif eq[0] == '/':
        answer = reduce(divide, nums_)

    elif eq[0] == 'square':
        answer = square(nums_)

    elif eq[0] == 'cube':
        answer = cube(nums_)

    elif eq[0] == 'pow':
        answer = power(nums_)

    elif eq[0] == 'mod':
        answer = mod(nums_)

    print('{:.3f}'.format(answer))
