# Name: 
# KUID: 
# LAB Session (Day/Time): 
# LAB Assignment: 
# Description:
#
#
#
# Collaborators/Sources:

# Note: if you are working in python, you are
# REQUIRED to call this function to get your
# input, so all assignments are consistant
# Returns a matrix in standard matrix notation:
# M[x][y] is row x, (top to bottom, starting at 0)
# and column y (left to right, starting at 0)
# for example, a 3x3 matrix is
# |(0,0) (0,1) (0,2)|
# |(1,0) (1,1) (1,2)|
# |(2,0) (2,1) (2,2)|
import numpy as np

def get_matrix(ints=False):
    """ 
    Takes a matrix of numbers from the user. Each row can be 
    separated by commas and/or spaces. A blank line ends the input.

    If ints=False, the function returns a matrix of strings. 
    If ints=True, they will be cast to int instead
    """
    print("Enter your matrix, with a blank line to end:")
    x = input()
    items = x.replace(","," ").split()
    length = len(items)
    matrix = []
    while(x.strip()):
        items = x.replace(","," ").split()
        if len(items) != length:
            print("Error: row lengths are mismatched! Try again:")
            return get_matrix(ints)
        if not ints:
            matrix.append(items)
        else:
            row = []
            for entry in items:
                row.append(int(entry))
            matrix.append(row)
        x = input()
    return matrix

# OPTIONAL: Helper function to print a 2-D matrix
def print_matrix(m):
    for row in m:
        for item in row:
            print(item, end=" ")
        print()

# Example
def main():
    m = get_matrix(False)
    print("Got: ")
    print_matrix(m)

main()
