#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    This function calculates the factorial of a given number using recursion.

    Parameters:
    n (int): The number for which the factorial is calculated.
             It must be a non-negative integer.

    Returns:
    int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get the number from the command-line arguments
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
