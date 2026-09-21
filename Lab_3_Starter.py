# Name: Zoey Spies
# KUID: 3136594
# LAB Session (Day/Time): Monday 11AM
# LAB Assignment: Lab 3
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

# multiply matrix without using numpy
def multiply_matrix(m,n):
    result = [] # initialize result matrix
    for i in range(len(m)): # iterate through rows of m
        row = [] # initialize row of result matrix
        for j in range(len(n[0])): # iterate through columns of n
            value = 0 # initialize value of result matrix
            for k in range(len(n)): # iterate through rows of n
                if m[i][k] == 1 and n[k][j] == 1: # if both values are 1, set value to 1
                    value = 1
                    break
            row.append(value) # append value to row of result matrix
        result.append(row) # append row to result matrix
    return result # return result matrix

# Example
def main():
    m = get_matrix(True) # get first matrix from user
    print("Got:") # print first matrix
    print_matrix(m)

    n = get_matrix(True) # get second matrix from user
    print("Got:") # print second matrix
    print_matrix(n)

    result = multiply_matrix(m, n) # multiply the two matrices
    print("Result:") # print result of multiplication
    print_matrix(result)
main()
