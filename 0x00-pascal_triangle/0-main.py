#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    # Edge test case 1: n = 0
    print("Pascal's triangle when n = 0:")
    print_triangle(pascal_triangle(0))
    print()
    
    # Edge test case 2: n = -5
    print("Pascal's triangle when n = -5:")
    print_triangle(pascal_triangle(-5))
    print()
    
    # Edge test case 3: n = 1
    print("Pascal's triangle when n = 1:")
    print_triangle(pascal_triangle(1))
    print()
    
    # Edge test case 4: n = 2
    print("Pascal's triangle when n = 2:")
    print_triangle(pascal_triangle(2))
    print()
