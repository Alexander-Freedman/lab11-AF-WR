"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math as m
# First example
def add(a, b): 
    return a + b

def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b
def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError
    return math.log(b, a)
def exp(a, b):
    return a ** b


def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


def logarithm(a, b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError
    return m.log(b, a)

def exponent(a, b):
    return ab



