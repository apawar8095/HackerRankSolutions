import math
import os
import random
import re
import sys

def missingCharacters(s):
    # Initialize lists to store missing digits and characters
    missing_digits = []
    missing_chars = []

    # Iterate through lowercase letters and digits
    for char in '0123456789':
        if char not in s:
            missing_digits.append(char)

    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            missing_chars.append(char)

    # Sort the missing digits and characters
    missing_digits.sort()
    missing_chars.sort()

    # Combine and return the result with spaces after each character
    result = ''.join([char + '' for char in missing_digits + missing_chars])
    return result.rstrip()  # Remove the trailing space


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     s = input()
#     result = missingCharacters(s)
#     fptr.write(result + '\n')
#     fptr.close()
