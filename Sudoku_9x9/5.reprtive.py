allsudokus = set()
sudoku = []
possible = []
s = 1
for i in range(9):
    possible.append([])
    for j in range(9):
        possible[i].append([])
solved = False
def retStringOfSudoku():
    global sudoku
    st = ''
    for i in range(9):
        for j in range(9):
            st += str(sudoku[i][j])
    return st
def inputsudoku():
    global sudoku
    for i in range(9):
        inp = input()
        sudoku.append([])
        for j in inp:
            if j != '.':
                sudoku[i].append(int(j))
            else:
                sudoku[i].append(0)
    allsudokus.add(retStringOfSudoku())
def printsudoku():
    global sudoku
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
def solve():
    global sudoku,possible,solved,allsudokus,s
    if check() == True and solved == False:
        #AC3
        for i in range(9):
            for j in range(9):
                for k in possible[i][j]:
                    if sudoku[i][j] == 0:
                        sudoku[i][j] = k
                        fillPossibleNode(i,j)
                        if fcCheck(i,j) == False:
                            possible[i][j].remove(k)
                        sudoku[i][j] = 0
                        fillPossibleNode(i,j)
        #is a list that keeps the minimum remaining variable sorted
        l = []
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] != 0 : continue
                l.append((len(possible[i][j]),i,j))
        l = sorted(l)
        for le,i,j in l:
            if len(possible[i][j]) > 1:
                listOfpossibles = []
                for k in possible[i][j]:
                    sudoku[i][j] = k
                    q = fillPossibleNode(i,j)
                    listOfpossibles.append((q,k))
                    sudoku[i][j] = 0
                    fillPossibleNode(i,j)
                listOfpossibles = sorted(listOfpossibles)
                for e,k in reversed(listOfpossibles):
                    sudoku[i][j] = k
                    fillPossibleNode(i,j)
                    s += 1
                    if allsudokus.intersection(retStringOfSudoku()) != set():
                        sudoku[i][j] = 0
                        fillPossibleNode(i,j)
                        continue
                    allsudokus.add(retStringOfSudoku())
                    solve()
                    if solved == True : return
                    sudoku[i][j] = 0
                    fillPossibleNode(i,j)
            else:
                sudoku[i][j] = possible[i][j][0]
                fillPossibleNode(i,j)
                s += 1
                if allsudokus.intersection(retStringOfSudoku()) != set():
                    sudoku[i][j] = 0
                    fillPossibleNode(i,j)
                    continue
                allsudokus.add(retStringOfSudoku())
                solve()
                if solved == True : return
                sudoku[i][j] = 0
                fillPossibleNode(i,j)
def fillPossibleNode(x,y):
    global sudoku,possible
    sum = 0
    lis = [[0,1,2],[3,4,5],[6,7,8]]
    #column
    j = y
    for i in range(9):
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
        for ii in lis[i//3]:
            for jj in lis[j//3]:
                if l.count(sudoku[ii][jj]) == 1:
                    l.remove(sudoku[ii][jj])
        possible[i][j] = l
        sum += len(possible[i][j])
    #row
    i = x
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
    #3*3
    for i in lis[x//3]:
        for j in lis[y//3]:
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
def fillPossibleArray():    
    global sudoku,possible
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
def fcCheck(x,y):
    global sudoku,possible
    j = y
    for i in range(9):
        if sudoku[i][j] != 0:
            continue
        if possible[i][j] == []:
            return False
    i = x
    for j in range(9):
        if sudoku[i][j] != 0:
            continue
        if possible[i][j] == []:
            return False
    lis = [[0,1,2],[3,4,5],[6,7,8]]
    for i in lis[x//3]:
        for j in lis[y//3]:
            if sudoku[i][j] != 0:
                continue
            if possible[i][j] == []:
                return False
    return True
def check():
    global sudoku,solved,possible
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
    if allNonZero() == True:
        solved = True
    return True
def allNonZero():
    global sudoku
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return False
    return True
#--------------------------------MAIN FUNCTION--------------------------------
inputsudoku()
fillPossibleArray()
solve()
printsudoku()
print(len(allsudokus), s)
# for i in range(9):
#     for j in range(9):
#         print(sudoku[i][j],end='')
#     print()