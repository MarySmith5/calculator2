"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

from functools import reduce
while True:
    
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
        else:
            print("Try again using only digits following the operator.")
            continue


    if eq[0] == '+':

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
