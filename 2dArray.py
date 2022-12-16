#  File: Spiral.py

#  Description: Creates a spiral that starts at center of dimension then counts outwards until the square

#  Student Name: Suren Bhakta

#  Student UT EID: ssb2943

#  Partner Name: Karim Ladak

#  Partner UT EID: Kal365

#  Course Name: CS 313E

#  Unique Number: 52520

#  Date Created: 09/01/2022

#  Date Last Modified: 09/06/2022

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
import sys


def create_spiral(n):
    n = int(n)
    # checks if even
    if n % 2 == 0:
        n = n + 1
    # creates 2d array
    spiral = [[0 for x in range(n)] for y in range(n)]
    count = 1
    # starting point is the center of the spiral
    row = n // 2
    col = n // 2
    index = n // 2
    mtval = n // 2
    # appends spiral until count equals square of dimension
    while count <= (n ** 2):
        # starts with one in the center of any dimension input
        for i in range(row, col + 1):
            spiral[index][i] = count
            count += 1
        if (count >= (n ** 2)):
            break
        col += 1
        # shifts "down" into the next list and continues to add to the count
        for i in range(index, mtval + 1):
            spiral[i][col] = count
            count += 1
        mtval += 1
        # Now instead of traversing to the right, the list is traversed backwards to follow the spiral
        for i in range(col, row - 1, -1):
            spiral[mtval][i] = count
            count += 1
        row -= 1
        for i in range(mtval, index - 1, -1):
            spiral[i][row] = count
            count += 1
        index -= 1
    return spiral


# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    n=int(n)
    sum = 0
    row = 0
    column = 0
    # calls bounds function to check if there is a number adjacent to the input
    # for loop checks every possible adjacent number

    for subspiral in spiral:
        if n in subspiral:
            row = spiral.index(subspiral)
            column = subspiral.index(n)
            if bounds(spiral, row, column + 1):
                sum += spiral[row][column + 1]
            if bounds(spiral, row + 1, column + 1):
                sum += spiral[row + 1][column + 1]
            if bounds(spiral, row - 1, column + 1):
                sum += spiral[row - 1][column + 1]
            if bounds(spiral, row - 1, column):
                sum += spiral[row - 1][column]
            if bounds(spiral, row + 1, column):
                sum += spiral[row + 1][column]
            if bounds(spiral, row - 1, column - 1):
                sum += spiral[row - 1][column - 1]
            if bounds(spiral, row, column - 1):
                sum += spiral[row][column - 1]
            if bounds(spiral, row + 1, column - 1):
                sum += spiral[row + 1][column - 1]
            return sum
    return 0


# checks to see if there is an adjacent number that exists inside the bound
def bounds(spiral, a, b):
    x=len(spiral)
    if a < 0 or a >=(x):
        return False
    elif b < 0 or b >=(x):
        return False
    return True


def main():
    # read the input file
    data = sys.stdin.read()
    data_list = data.split("\n")
    data_list.remove('')
    # create the spiral
    table = create_spiral(data_list[0])
    # removes dimension from being calculated
    data_list.pop(0)
    for data in data_list:
        print(sum_adjacent_numbers(table, data))


# print the result

if __name__ == "__main__":
    main()
