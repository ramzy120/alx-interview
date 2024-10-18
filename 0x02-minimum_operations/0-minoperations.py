#!/usr/bin/python3
"""
Minimum Operations
Given num n, write a method that calculates the fewest number of operations
needed to result in exactly n H characters in a file.
Prototype: def minOperations(n)
Returns an integer.
If n is impossible to achieve, return 0.
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to get n H characters.
    
    Parameters:
    n (int): The target number of 'H' characters.
    
    Returns:
    int: The minimum number of operations required.
         Returns 0 if n is less than 2.
    """
    if n < 2:
        return 0
    
    result = 0
    x = 2
    
    while n > 1:
        # Divide n by x as long as it is divisible
        while n % x == 0:
            result += x
            n //= x
        # Move to the next factor
        x += 1
    
    return result
