import copy
numberOfNodes = 0
solved = False
def inputsudoku(sudoku):
    for i in range(9):
        inp = input()
        sudoku.append([])
        for j in inp:
            if j != '.':
                sudoku[i].append(int(j))
            else:
                sudoku[i].append(0)
def printsudoku(sudoku):
    print()
    for i in range(9):
        print(' ',end='')
        for j in range(9):
            print(sudoku[i][j],end=' ')
            if j % 3 == 2 and j != 8 :
                print('|', end=' ')
        print()
        if i % 3 == 2 and i != 8 :
            print('-',end='')
            for j in range(9):
                print('--',end='')
                if j % 3 == 2 and j != 8 :
                    print('|', end='-')
            print()
def solve(x,y,sudoku,possible): 
    global solved,numberOfNodes
    numberOfNodes += 1
    sudokuCopy = copy.deepcopy(sudoku)
    possibleCopy = copy.deepcopy(possible)
    l = []
    for i in range(9):
        for j in range(9):
            if sudokuCopy[i][j] != 0 : continue
            l.append((len(possibleCopy[i][j]),i,j))
    l = sorted(l)
    le,i,j = l[0] # len(possible[i][j]),i,j
    if le > 1 :
        listOfpossibles = []
        for k in possibleCopy[i][j]:
            sudokuCopy[i][j] = k
            q = fillPossibleArray(sudokuCopy,possibleCopy)
            listOfpossibles.append((q,k)) # number of all possibles and the number of that cell
            sudokuCopy[i][j] = 0
            fillPossibleArray(sudokuCopy,possibleCopy)
        listOfpossibles = sorted(listOfpossibles)
        for e,k in reversed(listOfpossibles):
            sudokuCopy[i][j] = k
            fillPossibleArray(sudokuCopy, possibleCopy)
            if check(sudokuCopy,possibleCopy) == True and solved == False:
                solve(l[1][1],l[1][2],sudokuCopy,possibleCopy)
            if solved == True : 
                return
    else:
        for k in possibleCopy[i][j]:
            sudokuCopy[i][j] = k
            fillPossibleArray(sudokuCopy, possibleCopy)
            if check(sudokuCopy,possibleCopy) == True and solved == False:
                solve(l[1][1],l[1][2],sudokuCopy,possibleCopy)
            if solved == True : 
                return
def fillPossibleArray(sudoku, possible):  
    sum = 0
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                continue
            #list of possible numbers
            l = [1,2,3,4,5,6,7,8,9]
            #row
            for k in range(9):
                if l.count(sudoku[i][k]) == 1:
                    l.remove(sudoku[i][k])
            #column
            for k in range(9):
                if l.count(sudoku[k][j]) == 1:
                    l.remove(sudoku[k][j])
            #3*3
            lis = [[0,1,2],[3,4,5],[6,7,8]]
            for ii in lis[i//3]:
                for jj in lis[j//3]:
                    if l.count(sudoku[ii][jj]) == 1:
                        l.remove(sudoku[ii][jj])
            possible[i][j] = l
            sum += len(possible[i][j])
    return sum
def check(sudoku,possible):
    global solved
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                continue
            if possible[i][j] == []:
                return False
            #set of filled numbers
            #row
            se = set()
            se.add(sudoku[i][j])
            for k in range(9):
                if k == j or sudoku[i][k] == 0: continue
                if se.intersection({sudoku[i][k]}) == set():
                    se.add(sudoku[i][k])
                else:
                    return False
            #column
            se = set()
            se.add(sudoku[i][j])
            for k in range(9):
                if k == i  or sudoku[k][j] == 0: continue
                if se.intersection({sudoku[k][j]}) == set():
                    se.add(sudoku[k][j])
                else:
                    return False
            #3*3
            se = set()
            se.add(sudoku[i][j])
            lis = [[0,1,2],[3,4,5],[6,7,8]]
            for ii in lis[i//3]:
                for jj in lis[j//3]:
                    if (i == ii and j == jj)  or sudoku[ii][jj] == 0: continue
                    if se.intersection({sudoku[ii][jj]}) == set():
                        se.add(sudoku[ii][jj])
                    else:
                        return False
    if allNonZero(sudoku) == True:
        solved = True
        printsudoku(sudoku)
    return True
def allNonZero(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return False
    return True
#--------------------------------MAIN FUNCTION--------------------------------
sudoku = []
possible = []
for i in range(9):
    possible.append([])
    for j in range(9):
        possible[i].append([])
inputsudoku(sudoku)
fillPossibleArray(sudoku, possible)
l = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] != 0 : continue
        l.append((len(possible[i][j]),i,j))
l = sorted(l)
solve(l[0][1],l[0][2],sudoku,possible)
print(numberOfNodes)