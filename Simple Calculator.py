print('Simple Calculator')

import math
def add(x , y):
    return x + y

def subtract(x , y):
    return x - y

def multiply(x  , y):
    return x * y

def divide( x , y):
    if   y == 0 :
        return "Invalid value for denominator, cant't divide by 0!"
    else:
        return x / y

def square(x):
    return x ** 2

def power(x , y):
    return x ** y

def SqureRoot(x):
    return math.sqrt(x)

from Simplecalculator import subtract


def test_subtract():
    results = subtract(10, 7)
    assert results == 3








