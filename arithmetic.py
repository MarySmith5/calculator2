"""Functions for common math operations."""
from functools import reduce

def add(num_list):
    """Return the sum of the two inputs."""
  
    return sum(num_list)


def subtract(num_list):
    """Return the second number subtracted from the first."""
    diff = num_list[0] * 2
    for num in num_list:
        diff = diff - num
    return diff


def multiply(num_list):
    """Multiply the two inputs together."""
    product = 1
    for num in num_list:
        product = product * num
    return product

def divide(num1, num2):
    """Divide the first input by the second and return the result."""
 
    return  num1/num2

def square(num_list):
    """Return the square of the input."""
    return num_list[0]**2

def cube(num_list):
    """Return the cube of the input."""
    return num_list[0]**3

def power(num_list):
    """Raise num1 to the power of num2 and return the value."""
    return num_list[0]**num_list[1]

def mod(num_list):
    """Return the remainder of num1 / num2."""
    return num_list[0]% num_list[1]