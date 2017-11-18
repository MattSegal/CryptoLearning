"""
Extended Euclidean Algorithm
----------------------------
Solves the linear Diophantine equation usting the extended Euclidean algorithm.
Given two integers, a and b, find the values x and y such that:

    GCD(a, b) = ax + by

Usage:      python euclid.py <integer1> <integer2>
Example:    python euclid.py 274 63
Run tests:  python -m unittest discover
"""

def extended_euclid(a, b):
    """
    Solve extended Euclidean algorithm for integers a and b
    returns (gcd, x, y)
    """
    # Handle base case
    if a == 0:
        return (b, 0, 1)

    # Handle recursive case
    lower_a = b % a
    lower_b = a

    gcd, x, y = extended_euclid(lower_a, lower_b)
    
    next_x = y - (b // a) * x
    next_y = x

    return gcd, next_x, next_y


if __name__ == '__main__':
    # Runs the program when called from the command line
    import sys
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    gcd, x, y = euclid(a, b)
    print(
        "\n\tThe solution for GCD(a, b) = ax + by"
        "\n\twhere a={} and b={}"
        "\n\tis x={} and y={}"
    ).format(a, b, x, y)
