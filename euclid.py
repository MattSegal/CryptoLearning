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
    print('\ngcd({a}, {b}) = {a}x + {b}y'.format(a=a, b=b))

    # Handle base case - b is the gcd
    if a == 0:
        print('\n===== base case =====')
        return (b, 0, 1)

    # Handle recursive case
    lower_a = b % a
    lower_b = a
    print('\nlower a is {}\nlower b is {}'.format(a, b))

    gcd, x, y = extended_euclid(lower_a, lower_b)
    print('\n{} = {}*{} + {}*{}'.format(gcd, lower_a, x, lower_b, y))

    next_x = y - (b // a) * x
    next_y = x
    print('\nnext x is {}\nnext y is {}'.format(next_x, next_y))

    return gcd, next_x, next_y


if __name__ == '__main__':
    # Runs the program when called from the command line
    import sys
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    gcd, x, y = extended_euclid(a, b)
    print(
        "\nThe solution for GCD(a, b) = ax + by"
        "\nwhere a={} and b={}"
        "\nis x={} and y={}"
    ).format(a, b, x, y)
