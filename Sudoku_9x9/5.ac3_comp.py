import copy
# nubner of nodes that we create and show at the end of program
NUMBER_OF_NODES = 0
# if the algo find the solution this variable will become True
SOLVED = False

'''
input the sudoku from keyboard, the sample format is :

..1243..8
.4.6.....
3.8..5...
8.4.....1
.7..3..8.
2.....4.5
...3..6.2
.....6.1.
4..8129..

for empty sudoku :
.........
.........
.........
.........
.........
.........
.........
.........
.........

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
    # make a copy of previous sudoku
    sudoku_copy = copy.deepcopy(sudoku)
    possible_copy = copy.deepcopy(possible)

    # AC-3
    # for each possibility put that number in cell
    # and check whether this possiblity is solvable or not
    # in the next step
    
    # in this algo (AC-3) each time one possibility of one cell
    # changed we should check all the other affected cells again
    # so we keep all the cell in a queue and each time a cell changes
    # the affected cells (row, column, 3x3) should be checked again
    # so we check it again by adding them in the queue
    
    # set of all cells in set_all to make sure every cell at least 
    # one time checked
    set_all = set()
    for i in range(9):
        for j in range(9):
            set_all.update({(i,j)})
    
    # a queue to loop on it to check all the cells and the
    #  affected cells
    queue = []
    for i in range(9):
        for j in range(9):
            # at first check the cells that only have
            # one possibility
            if sudoku_copy[i][j] == 0 and len(possible_copy[i][j]) == 1:
                queue.append((i, j))
                set_all.remove((i, j))
    
    p = 0
    # if nothing is in queue
    if p >= len(queue) and set_all != set():
        queue.append(set_all.pop())
        
    # traverse the queue until end of the queue
    # and we don't have any cell in set_all
    while(set_all != set()):
        # place all the possibilities in cell and check
        # whether it is solvable or not and if it's not
        # solvable append the affected (row, column, 3x3)
        # cells of that cell
        for k in possible_copy[queue[p][0]][queue[p][1]]:
            # new copy of sudoku and possible
            sudoku1 = copy.deepcopy(sudoku_copy)
            possible1 = copy.deepcopy(possible_copy)

            sudoku1[queue[p][0]][queue[p][1]] = k
            fillPossibleNode(queue[p][0], queue[p][1], sudoku1, possible1)
            if not fcCheck(queue[p][0], queue[p][1], sudoku1, possible1):
                possible_copy[queue[p][0]][queue[p][1]].remove(k)
                # the row (affected cells)
                for i in range(9):
                    if sudoku_copy[queue[p][0]][i] == 0:
                        queue.append((queue[p][0], i))
                        set_all.discard((queue[p][0], i))

                # the column (affected cells)
                for j in range(9):
                    if sudoku_copy[i][queue[p][0]] == 0:
                        queue.append((i,queue[p][0]))
                        set_all.discard((i,queue[p][0]))

                # the 3x3 affected cells
                lis = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
                for ii in lis[queue[p][0]//3]:
                    for jj in lis[queue[p][1]//3]:
                        if sudoku_copy[ii][jj] == 0:
                            queue.append((ii, jj))
                            set_all.discard((ii, jj))
            elif SOLVED:
                return
        p += 1
        if p >= len(queue) and set_all != set():
            queue.append(set_all.pop())
    
    # mrv part, a list to save all possibilites from all cells
    l = []
    for i in range(9):
        for j in range(9):
            if sudoku_copy[i][j] != 0:
                continue
            l.append((len(possible_copy[i][j]), i, j))
    # we sort the possibilities to find out which cell
    # has the minimum possiblitie so if one cell has
    # like 1, 2 possibility we fill them first
    l = sorted(l)

    len_of_cell, i, j = l[0]
    # lcv part
    # if the possiblity of the cell is more than one
    # so we choose the one that prudoces less possibilites
    # in the next step 
    if len_of_cell > 1:
        list_of_possibles = []
        # we select each possibility for cell
        # and then we choose the lcv
        for k in possible_copy[i][j]:
            # we keep the original sudoku
            sudoku_copy2 = copy.deepcopy(sudoku_copy)
            possible_copy2 = copy.deepcopy(possible_copy)
            sudoku_copy2[i][j] = k
            q = fillPossibleNode(i, j, sudoku_copy2, possible_copy2)
            # number of all possibilities and the number of that cell
            list_of_possibles.append((q, k)) 
        # sort the list_of_possibles
        list_of_possibles = sorted(list_of_possibles,reverse=True)

        for q,k in list_of_possibles:
            sudoku_copy[i][j] = k
            # fill(change) the possibilities of other cells
            fillPossibleNode(i, j, sudoku_copy, possible_copy)
            # if the number we place is ok and the sudoku hasn't been solved
            if fcCheck(i, j, sudoku_copy, possible_copy) and not SOLVED:
                # go to the next cell
                solve(l[1][1], l[1][2], sudoku_copy, possible_copy)
            if SOLVED:
                return
    # if the possible_copy was empty do nothing
    elif possible_copy[i][j] != []:
        sudoku_copy[i][j] = possible_copy[i][j][0]
        # fill(change) the possibilities of other cells
        fillPossibleNode(i, j, sudoku_copy, possible_copy)
        # if the number we place is ok and the sudoku hasn't been solved
        if fcCheck(i, j, sudoku_copy, possible_copy) and not SOLVED:
            # go to the next cell
            solve(l[1][1], l[1][2], sudoku_copy, possible_copy)
        if SOLVED:
            return

# for inner loop i use this function
# because each change only change some of
# the cells not all of them
def fillPossibleNode(x, y, sudoku, possible):
    sum = 0
    lis = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    #column
    j = y
    for i in range(9):
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
        for ii in lis[i//3]:
            for jj in lis[j//3]:
                if sudoku[ii][jj] in l:
                    l.remove(sudoku[ii][jj])
        possible[i][j] = l
    #row
    i = x
    for j in range(9):
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
        for ii in lis[i//3]:
            for jj in lis[j//3]:
                if sudoku[ii][jj] in l:
                    l.remove(sudoku[ii][jj])
        possible[i][j] = l
    #3*3
    for i in lis[x//3]:
        for j in lis[y//3]:
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
            for ii in lis[i//3]:
                for jj in lis[j//3]:
                    if sudoku[ii][jj] in l:
                        l.remove(sudoku[ii][jj])
            possible[i][j] = l
    for i in range(9):
        for j in range(9):
            sum += len(possible[i][j])
    return sum

def fillPossibleArray(sudoku, possible):
    # sum of all the possiblities of all cells
    sum = 0
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
            # for this cell how many possiblities do we have
            sum += len(possible[i][j])
    return sum

# this function checks only the affected cells
def fcCheck(x, y, sudoku, possible):
    global SOLVED
    # the row of changed cell
    j = y
    for i in range(9):
        if sudoku[i][j] != 0:
            continue
        if possible[i][j] == []:
            return False
    # the column of changed cell
    i = x
    for j in range(9):
        if sudoku[i][j] != 0:
            continue
        if possible[i][j] == []:
            return False
    # the 3x3 of changed cell
    lis = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    for i in lis[x//3]:
        for j in lis[y//3]:
            if sudoku[i][j] != 0:
                continue
            if possible[i][j] == []:
                return False
    # if all the cells is not zero so the sudoku is solved
    if allNonZero(sudoku):
        SOLVED = True
        printsudoku(sudoku)
    # if everything is ok so return True
    return True

# check if the numbers in sudoku is ok True for ok and False for not ok
def check(sudoku, possible):
    global SOLVED
    # for each cells in sudoku
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                continue
            # forward checknig part
            # if for an empty cell we don't have
            # any possibility so the answer is werong
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

if check(sudoku, possible):
    # solve from location that has the least possible numbers with sudoku and possible
    solve(l[0][1], l[0][2], sudoku, possible)
    # at the end print the number of nodes that we make through the algo with bachtrack
    print()
    print('Number of nodes : ', NUMBER_OF_NODES)
else:
    print('The sudoku can not be solved !')
