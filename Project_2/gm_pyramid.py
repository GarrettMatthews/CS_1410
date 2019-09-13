# Garrett Matthews
# Project 2: Human Pyramid

# I declare that the following source code was written solely by me. I understand that copying any source code, #
# in whole or in part, constitutes cheating, and that I will receive a zero on this project if I am found in violation #
# of this policy. #


# Calculate the weight a certain person in row and column (r,c) is carrying using recursion

# Because sys.argv[1] is being used, to properly run this program the command line or terminal must be used as indicated
# in the following example: python3 gm_pyramid.py <Number of rows you want computed>

# Importing modules to be used
import sys
import time
# Initializing the cache dictionary
cache = {}
# Making the weightOn function
def weightOn(r,c):
    """Calculates the weight a person in row r and column c is feeling"""
    # First checking if the value is already recorded in the cache
    if (r,c) in cache:
        return cache[(r,c)]
    # Computing the value if it is not already present
    else:
        if c > (r):
            return(0)
        elif c < 0:
            return(0)
        elif r == 0:
            return("{:.2f}".format(0))
        else:
            weight = 200
            if c == 0 or c == r:
                carry = ((200 / 2) + (float(weightOn(r -1, c)) / 2) + (float(weightOn(r -1, c -1))/ 2))
            else:
                carry = ((400 / 2) + (float(weightOn(r - 1, c)) / 2) + (float(weightOn(r - 1, c - 1)) / 2))
            # Storing the computed value to the cache
            cache[(r,c)] = ("{:.2f}".format(carry))
            return("{:.2f}".format(carry))

# Making the main function
def main(argv):
    for i in range(argv):
        for q in range(argv):
            if q <= i:
                weights = (weightOn(i,q))
                print(weights, end = " ")
        print()
# Initializing the program to calculate how much time it takes, as well as build a pyramid of information
if __name__ == '__main__':
    start = time.perf_counter()
    main(int(sys.argv[1]))
    stop = time.perf_counter()
    print()
    print("Elapsed time:",stop-start,'seconds')


