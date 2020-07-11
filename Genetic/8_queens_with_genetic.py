import random
def makeChessBoards(chessBoards):
    for i in range(8):
        l = [1,2,3,4,5,6,7,8]
        random.shuffle(l)
        chessBoards.append(l)
def printChessBoards(chessBoards):
    for i in range(8):
        print(chessBoards[i])
#checks wheather the list is the answer or not
def check(chessBoard):
    #each queen in one col
    for i in range(8):
        if chessBoard.count(i+1) != 1:
            return False
    #diagonal
    for i in range(8):
        for j in range(8):
            if i == j : continue
            diffX = abs(i - j)
            diffY = abs(chessBoard[i] - chessBoard[j])
            if diffX == diffY : return False
    return True
def value(chessBoard):
    sum = 0
    for i in range(8):
        s = chessBoard.count(i+1)
        if s >= 2:
            sum += (s-1)
    for i in range(8):
        for j in range(i,8):
            if i == j : continue
            diffX = abs(i - j)
            diffY = abs(chessBoard[i] - chessBoard[j])
            if diffX == diffY : sum += 1
    # 28 is when no queen hits another one
    return (28 - sum)
#-----------------------MAIN FUNCTION-----------------------
chessBoards = []
makeChessBoards(chessBoards)
for _ in range(50000):
    #check the 8 chessBoards
    for i in range(8):
        if check(chessBoards[i]) == True:
            print(chessBoards[i])
            exit(0)
    #calc the values
    listOfValues = []
    for i in range(8):
        listOfValues.append(value(chessBoards[i]))
    #Selection
    chessBoards1 = []
    allValues = []
    sum = 0
    for i in range(8):
        sum += listOfValues[i]
        allValues.append(sum)
    for i in range(8):
        try:
            x = random.randint(1,allValues[7])
            for j in range(8):
                if x <= allValues[j]:
                    chessBoards1.append(chessBoards[j])
                    break
        except:
            chessBoards1 = chessBoards
            break
    #Crossover
    for _ in range(4):
        a = random.randint(0,7)
        b = random.randint(0,7)
        n1 = random.randint(0,7)
        n2 = random.randint(n1,7)
        n3 = random.randint(0,7)
        for i in range(n1,n2):
            chessBoards1[b][i],chessBoards1[a][(i+n3)%8] = chessBoards1[a][(i+n3)%8],chessBoards1[b][i]
    #Mutation
    for _ in range(8):
        i = random.randint(0,7)
        j = random.randint(0,7)
        new = random.randint(1,8)
        chessBoards1[i][j] = new
    chessBoards = chessBoards1
printChessBoards(chessBoards)
print(listOfValues)
