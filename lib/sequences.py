#!/usr/bin/env python3

def print_fibonacci(length):
    """Print the first `length` Fibonacci numbers as a Python list.

    Examples:
        length = 0 -> prints []\n
        length = 1 -> prints [0]\n
        length = 2 -> prints [0, 1]\n
    """
    if length <= 0:
        print([])
        return

    # build fibonacci list
    fib = [0]
    if length == 1:
        print(fib)
        return

    fib.append(1)
    while len(fib) < length:
        fib.append(fib[-1] + fib[-2])

    print(fib)