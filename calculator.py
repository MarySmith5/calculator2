"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    equation = input('Enter equation: ')
    eq = equation.split(' ')

    if eq[0].lower().startswith('q'):
        print("Exiting calculator")
        break

    elif eq[0] == '+':
        answer = add(float(eq[1]), float(eq[2]))

    elif eq[0] == '-':
        answer = subtract(float(eq[1]), float(eq[2]))
    
    elif eq[0] == '*':
        answer = multiply(float(eq[1]), float(eq[2]))

    elif eq[0] == '/':
        answer = divide(float(eq[1]), float(eq[2]))

    elif eq[0] == 'square':
        answer = square(float(eq[1]))

    elif eq[0] == 'cube':
        answer = cube(float(eq[1]))

    elif eq[0] == 'pow':
        answer = power(float(eq[1]), float(eq[2]))

    elif eq[0] == 'mod':
        answer = mod(float(eq[1]), float(eq[2]))
