def add(a, b):
    return a + b  

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def power(a, b):
    return a ** b
def modulus(a, b):
    return a % b
def floor_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a // b
def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number.")
    return a ** 0.5
def logarithm(a, base=10):
    import math
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive values.")
    return math.log(a, base)
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
