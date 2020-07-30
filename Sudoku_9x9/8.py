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
    #AC3
    setAll = set()
    for i in range(9):
        for j in range(9):
            setAll.update({(i,j)})
    queue = []
    for i in range(9):
        for j in range(9):
            if sudokuCopy[i][j] == 0 and len(possibleCopy[i][j]) == 1:
                queue.append((i,j))
                setAll.remove((i,j))
    p = 0
    if p >= len(queue):
        try:queue.append(setAll.pop())
        except:pass
    while(setAll != set()):
        for k in possibleCopy[queue[p][0]][queue[p][1]]:
            sudoku1 = copy.deepcopy(sudokuCopy)
            possible1 = copy.deepcopy(possibleCopy)
            sudoku1[queue[p][0]][queue[p][1]] = k
            fillPossibleNode(queue[p][0],queue[p][1],sudoku1,possible1)
            if fcCheck(queue[p][0],queue[p][1],sudoku1,possible1) == False:
                possibleCopy[queue[p][0]][queue[p][1]].remove(k)
                for i in range(9):
                    if sudokuCopy[queue[p][0]][i] == 0:
                        queue.append((queue[p][0],i))
                        try:setAll.remove((queue[p][0],i))
                        except:pass
                for j in range(9):
                    if sudokuCopy[i][queue[p][0]] == 0:
                        queue.append((i,queue[p][0]))
                        try:setAll.remove((i,queue[p][0]))
                        except:pass
                lis = [[0,1,2],[3,4,5],[6,7,8]]
                for ii in lis[queue[p][0]//3]:
                    for jj in lis[queue[p][1]//3]:
                        if sudokuCopy[ii][jj] == 0:
                            queue.append((ii,jj))
                            try:setAll.remove((ii,jj))
                            except:pass
        p += 1
        if p >= len(queue):
            try:queue.append(setAll.pop())
            except:pass
    #is a list that keeps the minimum remaining variable sorted
    l = []
    for i in range(9):
        for j in range(9):
            if sudokuCopy[i][j] != 0 : continue
            l.append((len(possibleCopy[i][j]),i,j))
    l = sorted(l)
    le,i,j = l[0] # len(possibleCopy[i][j]),i,j
    if le > 1 :
        listOfpossibles = []
        for k in possibleCopy[i][j]:
            sudoku1 = copy.deepcopy(sudokuCopy)
            possible1 = copy.deepcopy(possibleCopy)
            sudoku1[i][j] = k
            q = fillPossibleNode(i,j,sudoku1,possible1)
            listOfpossibles.append((q,k)) # number of all possibles and the number of that cell
        listOfpossibles = sorted(listOfpossibles)
        for e,k in reversed(listOfpossibles):
            sudokuCopy[i][j] = k
            fillPossibleNode(i,j,sudokuCopy, possibleCopy)
            if check(sudokuCopy,possibleCopy) == True and solved == False:
                solve(l[1][1],l[1][2],sudokuCopy,possibleCopy)
            if solved == True : 
                return
    else:
        if possibleCopy[i][j] != []:
            sudokuCopy[i][j] = possibleCopy[i][j][0]
            fillPossibleNode(i,j,sudokuCopy, possibleCopy)
            if check(sudokuCopy,possibleCopy) == True and solved == False:
                solve(l[1][1],l[1][2],sudokuCopy,possibleCopy)
            if solved == True : 
                return
def fillPossibleNode(x,y,sudoku,possible):
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
    #find hidden singles in Row
    for i in range(9):
        firstTime = set()
        secondAndMore = set()
        for j in range(9):
            for k in possible[i][j]:
                if firstTime.intersection({k}) == set():
                    firstTime.add(k)
                else:
                    secondAndMore.add(k)
        s = firstTime.symmetric_difference(secondAndMore) 
        #replace hidden singles with one possible
        if s != set():
            for k in s:
                for j in range(9):
                    if possible[i][j].count(k) == 1:
                        possible[i][j] = [k]
                        break
    #find hidden singles in Column
    for j in range(9):
        firstTime = set()
        secondAndMore = set()
        for i in range(9):
            for k in possible[i][j]:
                if firstTime.intersection({k}) == set():
                    firstTime.add(k)
                else:
                    secondAndMore.add(k)
        s = firstTime.symmetric_difference(secondAndMore) 
        #replace hidden singles with one possible
        if s != set():
            for k in s:
                for i in range(9):
                    if possible[i][j].count(k) == 1:
                        possible[i][j] = [k]
                        break
    #find hidden singles in 3*3
    lis = [[0,1,2],[3,4,5],[6,7,8]]
    for i in range(3):
        for j in range(3):
            #inside of a 3*3
            firstTime = set()
            secondAndMore = set()
            for ii in lis[i]:
                for jj in lis[j]:
                    for k in possible[ii][jj]:
                        if firstTime.intersection({k}) == set():
                            firstTime.add(k)
                        else:
                            secondAndMore.add(k)
            s = firstTime.symmetric_difference(secondAndMore) 
            #replace hidden singles with one possible
            if s != set():
                for k in s:
                    for ii in lis[i]:
                        for jj in lis[j]:
                            if possible[ii][jj].count(k) == 1:
                                possible[ii][jj] = [k]
                                break
    for i in range(9):
        for j in range(9):
            sum += len(possible[i][j])
    return sum
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
    #find hidden singles in Row
    for i in range(9):
        firstTime = set()
        secondAndMore = set()
        for j in range(9):
            for k in possible[i][j]:
                if firstTime.intersection({k}) == set():
                    firstTime.add(k)
                else:
                    secondAndMore.add(k)
        s = firstTime.symmetric_difference(secondAndMore) 
        #replace hidden singles with one possible
        if s != set():
            for k in s:
                for j in range(9):
                    if possible[i][j].count(k) == 1:
                        possible[i][j] = [k]
                        break
    #find hidden singles in Column
    for j in range(9):
        firstTime = set()
        secondAndMore = set()
        for i in range(9):
            for k in possible[i][j]:
                if firstTime.intersection({k}) == set():
                    firstTime.add(k)
                else:
                    secondAndMore.add(k)
        s = firstTime.symmetric_difference(secondAndMore) 
        #replace hidden singles with one possible
        if s != set():
            for k in s:
                for i in range(9):
                    if possible[i][j].count(k) == 1:
                        possible[i][j] = [k]
                        break
    #find hidden singles in 3*3
    lis = [[0,1,2],[3,4,5],[6,7,8]]
    for i in range(3):
        for j in range(3):
            #inside of a 3*3
            firstTime = set()
            secondAndMore = set()
            for ii in lis[i]:
                for jj in lis[j]:
                    for k in possible[ii][jj]:
                        if firstTime.intersection({k}) == set():
                            firstTime.add(k)
                        else:
                            secondAndMore.add(k)
            s = firstTime.symmetric_difference(secondAndMore) 
            #replace hidden singles with one possible
            if s != set():
                for k in s:
                    for ii in lis[i]:
                        for jj in lis[j]:
                            if possible[ii][jj].count(k) == 1:
                                possible[ii][jj] = [k]
                                break
    for i in range(9):
        for j in range(9):
            sum += len(possible[i][j])
    return sum
def fcCheck(x,y,sudoku,possible):
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
def check(sudoku,possible):
    global solved
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                continue
            if possible[i][j] == []:
                return False
    #row
    #set of filled numbers
    for i in range(9):
        se = set()
        for k in range(9):
            if sudoku[i][k] == 0: continue
            if se.intersection({sudoku[i][k]}) == set():
                se.add(sudoku[i][k])
            else:
                return False
    #column
    for j in range(9):
        se = set()
        for k in range(9):
            if sudoku[k][j] == 0: continue
            if se.intersection({sudoku[k][j]}) == set():
                se.add(sudoku[k][j])
            else:
                return False
    #3*3
    for i in range(0,9,3):
    	for j in range(0,9,3):
            se = set()
            lis = [[0,1,2],[3,4,5],[6,7,8]]
            for ii in lis[i//3]:
                for jj in lis[j//3]:
                    if sudoku[ii][jj] == 0: continue
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

"""
..1243..8
.4.6.....
3.8..5...
8.4.....1
.7..3..8.
2.....4.5
...3..6.2
.....6.1.
4..8129..
"""
