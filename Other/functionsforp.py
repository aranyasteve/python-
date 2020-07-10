def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


def mod(a, b):
    return a % b


def fact(a):
    factorial = 1
    for i in range(a,1,-1):
        factorial = factorial*i
    return factorial