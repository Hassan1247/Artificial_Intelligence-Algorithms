import copy
# nubner of nodes that we create and show at the end of program
NUMBER_OF_NODES = 0
# if the algo find the solution this variable will become True
SOLVED = False

# input the sudoku from keyboard, the sample format is :
'''
..1243..8
.4.6.....
3.8..5...
8.4.....1
.7..3..8.
2.....4.5
...3..6.2
.....6.1.
4..8129..
'''
def inputsudoku(sudoku):
    for i in range(9):
        inp = input()
        sudoku.append([])
        for j in inp:
            if j != '.':
                sudoku[i].append(int(j))
            else:
                sudoku[i].append(0)

# a function to print sudoku in a good format
def printsudoku(sudoku):
    print()
    for i in range(9):
        print(' ', end='')
        for j in range(9):
            print(sudoku[i][j], end=' ')
            if j % 3 == 2 and j != 8:
                print('|', end=' ')
        print()
        if i % 3 == 2 and i != 8:
            print('-', end='')
            for j in range(9):
                print('--', end='')
                if j % 3 == 2 and j != 8:
                    print('|', end='-')
            print()

# solve the sudoku using only backtrack and forward checking (backtrack part)
def solve(x, y, sudoku, possible):
    global SOLVED, NUMBER_OF_NODES
    NUMBER_OF_NODES += 1
    # if the number we place is ok and the sudoku hasn't been solved
    if check(sudoku, possible) and not SOLVED:
        # make a copy of previous sudoku
        sudoku_copy = copy.deepcopy(sudoku)
        possible_copy = copy.deepcopy(possible)

        # mrv part, a list to save all possibilites from all cells
        l = []
        for i in range(9):
            for j in range(9):
                if sudoku_copy[i][j] != 0:
                    continue
                l.append((len(possible_copy[i][j]), i, j))
        l = sorted(l)

        len_of_cell, i, j = l[0]
        # fill the empty cell with 1 to 9
        for k in possible_copy[i][j]:
            sudoku_copy[i][j] = k
            # fill(change) the possibilities of other cells
            fillPossibleArray(sudoku_copy, possible_copy)
            # i have check again because i want go to the next cell
            if check(sudoku_copy, possible_copy) and not SOLVED:
                # go to the next cell
                solve(l[1][1], l[1][2], sudoku_copy, possible_copy)
            if SOLVED:
                return

# in this function we fill the possible array with possible numbers that can place in a cell
def fillPossibleArray(sudoku, possible):
    # for all cells
    for i in range(9):
        for j in range(9):
            # if the cell is not empty (have a number) do nothing
            # (a filled cell doesn't have possiblities)
            if sudoku[i][j] != 0:
                continue
            #list of possible numbers
            l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            #row
            for k in range(9):
                if sudoku[i][k] in l:
                    l.remove(sudoku[i][k])
            #column
            for k in range(9):
                if sudoku[k][j] in l:
                    l.remove(sudoku[k][j])
            #3*3
            lis = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
            for ii in lis[i//3]:
                for jj in lis[j//3]:
                    if sudoku[ii][jj] in l:
                        l.remove(sudoku[ii][jj])
            possible[i][j] = l

# check if the numbers in sudoku is ok True for ok and False for not ok
def check(sudoku, possible):
    global SOLVED
    # for each cells in sudoku
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                continue
            # forward checknig part
            if possible[i][j] == []:
                return False
    #row
    for i in range(9):
        #set of filled numbers
        se = set()
        for k in range(9):
            if sudoku[i][k] == 0:
                continue
            if se.intersection({sudoku[i][k]}) == set():
                se.add(sudoku[i][k])
            else:
                return False
    #column
    for j in range(9):
        se = set()
        for k in range(9):
            if sudoku[k][j] == 0:
                continue
            if se.intersection({sudoku[k][j]}) == set():
                se.add(sudoku[k][j])
            else:
                return False
    #3*3
    for i in range(0, 9, 3):
    	for j in range(0, 9, 3):
            se = set()
            lis = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
            for ii in lis[i//3]:
                for jj in lis[j//3]:
                    if sudoku[ii][jj] == 0:
                        continue
                    if se.intersection({sudoku[ii][jj]}) == set():
                        se.add(sudoku[ii][jj])
                    else:
                        return False
    # if all the cells is not zero so the sudoku is solved
    if allNonZero(sudoku):
        SOLVED = True
        printsudoku(sudoku)
    # if everything is ok so return True
    return True

# check if all the cells is full
def allNonZero(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return False
    return True

#--------------------------------MAIN FUNCTION--------------------------------

# create the lists
sudoku = []
possible = []

# fill the possible array with empty lists
for i in range(9):
    possible.append([])
    for j in range(9):
        possible[i].append([])
# get the sudoku
inputsudoku(sudoku)

fillPossibleArray(sudoku, possible)

# sort the possibleArray to choose the minimum value
# (first choose a cell with minimum options)
l = []
for i in range(9):
    for j in range(9):
        # if the cell is not empty so we don't have any possibility for that cell
        if sudoku[i][j] != 0:
            continue
        # number of possibilities, (location of the cell)
        l.append((len(possible[i][j]), i, j))
l = sorted(l)

# solve from location that has the least possible numbers with sudoku and possible
solve(l[0][1], l[0][2], sudoku, possible)
# at the end print the number of nodes that we make through the algo with bachtrack
print()
print('Number of nodes : ', NUMBER_OF_NODES)
