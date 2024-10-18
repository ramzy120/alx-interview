#!/usr/bin/python3
"""
Minimum Operations
Given num n, write a method that calculates the fewest number of operations
needed to result in exactly n H characters in a file
Prototype: def minOperations(n)
Returns an integer
if n is impossible to achieve, return 0
"""

def minOperations(n):
    """
    Function minOperations
    Calculates the fewest number of operations needed to get n H characters.
    
    Returns:
        An integer representing the minimum number of operations needed.
        Returns 0 if n is impossible to achieve.
    """
    if n < 2:
        return 0

    result = 0
    x = 2
    
    while n > 1:
        while n % x == 0:
            result += x
            n //= x  # Use integer division to avoid float issues
        x += 1
    
    return result
