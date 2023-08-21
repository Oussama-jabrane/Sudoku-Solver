table = [
    [9,0,3,0,0,0,0,6,8],
    [6,0,0,0,0,9,0,0,0],
    [0,5,0,0,0,0,0,0,7],
    [3,0,0,7,0,0,9,0,0],
    [0,0,6,4,0,0,0,5,1],
    [8,0,1,0,6,2,0,7,0],
    [0,0,8,0,4,0,0,1,0],
    [0,0,0,3,0,1,6,0,5],
    [1,0,0,0,0,0,0,3,4],
]


# Function that solves the Sudoku table using backtracking and recursion
def solve(table):
    find = find_empty_spot(table=table)
    if not find:
        return True
    else:
        row, col = find

    # Looping for each individual possible answer
    for i in range(1, 10):
        if is_valid(table, i, (row, col)):
            table[row][col] = i

            # If the answer is valid, the program returns True
            if solve(table):
                return True

            table[row][col] = 0

    return False


# Function that checks if the number can be put in the spot and either returns True or False
def is_valid(table, number, position):
    # Check the row
    for i in range(len(table[0])):
        if table[position[0]][i] == number and position[1] != i:
            return False

    # Check the column
    for i in range(len(table)):
        if table[i][position[1]] == number and position[0] != i:
            return False

    # Check which box we're in (the box is the 3x3 square)
    box_x = position[1] // 3
    box_y = position[0] // 3

    # Check if the number is already in the box
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if table[i][j] == number and (i, j) != position:
                return False

    # If all the tests (or cases) are passed, then the number can be put in the spot
    return True


# Make a function that gets the table and prints it like an actual Sudoku table (or board)
def print_table(table):
    for i in range(len(table)):
        # For every 3 columns, a space-filler will be printed
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(table[0])):
            # For every 3 numbers in the row, a separator will be printed
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(table[i][j])
            else:
                print(str(table[i][j]) + " ", end="")


# make a function that searches and finds empty spots
def find_empty_spot(table):
    # Looping for every row and column
    for i in range(len(table)):
        for j in range(len(table[0])):
            # Checking if the spot is empty
            if table[i][j] == 0:
                return (i, j)

    return None


# Print the table before solving it
print("\n")
print_table(table=table)
# Call the function that solves the Sudoku table
solve(table)
# Print the solved table
print("\n# # # # # # # # # # # #\n")
print_table(table=table)
