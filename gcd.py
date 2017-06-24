"""
Greatest Common Divisor - Finds the greatest common divisor of 2 integers

Usage:      python gcd.py <integer1> <integer2>
Example:    python gcd.py 42823 6409 => 17
Run tests:  python -m unittest discover
"""

def gcd(a, b):
    """
    Finds the greatest common divisor of
    two integers - a and b
    """
    big_number = max(a, b)
    small_number = min(a, b)

    remainder = 1
    while remainder > 0:
        # We want to find the factor and remainder in the equation
        # big_number = factor * small_number + remainder
        factor, remainder = divide(big_number, small_number)
        print "{} = {} * {} + {}".format(big_number, factor, small_number, remainder)
        
        big_number = small_number
        small_number = remainder if remainder > 0 else small_number

    return small_number


def divide(big_number, small_number):
    """
    Find factor and remainder in
    big_number = factor * small_number + remainder
    """
    factor = big_number / small_number
    remainder = big_number % small_number
    return factor, remainder


if __name__ == '__main__':
    # Runs the program when called from the command line
    import sys
    integer1 = int(sys.argv[1])
    integer2 = int(sys.argv[2])
    result = gcd(integer1, integer2)
    print "\n\tGCD of {} and {} is {}\n".format(integer1, integer2, result)
