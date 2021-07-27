"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

from functools import reduce
while True:
    equation = input('Enter equation: ')
    eq = equation.split(' ')
    nums_= []
    for item in eq[1:]:
        nums_.append(float(item))

    if eq[0].lower().startswith('q'):
        print("Exiting calculator")
        break

    elif eq[0] == '+':

        answer = add(nums_)

    elif eq[0] == '-':
        answer = subtract(nums_)
    
    elif eq[0] == '*':
        answer = multiply(nums_)

    elif eq[0] == '/':
        answer = reduce(divide(nums_), nums_, nums_[0])

    elif eq[0] == 'square':
        answer = square(nums_)

    elif eq[0] == 'cube':
        answer = cube(nums_)

    elif eq[0] == 'pow':
        answer = power(nums_)

    elif eq[0] == 'mod':
        answer = mod(nums_)

    print(answer)
