#!/usr/bin/python3
from random import shuffle

class Node(object):
    def __init__(self,data,pre = None):
        # the list of puzzle 
        self.data = data
        # pointer to previous node
        self.pre = pre 
        # h score of node
        self.hn = 0
        #  f score of node
        self.fn = 0
        if pre != None:
            # g score of node
            self.gn = pre.gn + 1
        else:
            # g score of the root
            self.gn = 0

# calculate the f score of the node
def calFn(node):
    dict = {0:(0,0), 1:(0,1), 2:(0,2), 3:(1,0), 4:(1,1), 5:(1,2), 6:(2,0), 7:(2,1), 8:(2,2)}
    h = 0
    # Manhattan distance of puzzle 
    for i in range(9):
        if node.data[i] == 0 :
            continue
        x,y = dict[i]
        xx,yy = dict[node.data[i] - 1]
        h += (abs(xx-x)+ abs(yy-y))
    node.hn = h
    node.fn = node.hn + node.gn

# shuffle the list of puzzle (shuffles the puzzle)
def makeRand():
    l = [1,2,3,4,5,6,7,8,0]
    shuffle(l)
    return l

# check that if the puzzle is solvable (it's a fuciton that you can find it on https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/)
def isSolvable(list):
    s = 0
    for i in reversed(range(0,9)):
        if list[i] == 0 :
            continue
        for j in range(i + 1,9):
            if list[j] == 0 :
                continue
            if list[i] > list[j]:
                s += 1
    if s % 2 == 0 :
        return True
    return False

# print the puzzle in a good shape 
def pp(lst):
    for i in range(3):
        for j in range(3):
            print(lst[j+ i * 3], end= ' ')
        print()

#-------------------------------------MAIN PART-------------------------------------
l = makeRand()
# make another puzzle till one is solvable
while not isSolvable(l):
    l = makeRand()
# create the first node
firstNode = Node(l)
calFn(firstNode)
# the list of nodes that we traverse through
array = []
# the list of all nodes that we produce
array2 = []
array.append(firstNode)
array2.append(firstNode.data)
i = array[0]
print(i.data)
dict = {0:(0,0), 1:(0,1), 2:(0,2), 3:(1,0), 4:(1,1), 5:(1,2), 6:(2,0), 7:(2,1), 8:(2,2)}

# the A* algorithm 
while True:
    # pop from the start of the array
    i = array[0]
    del array[0]
    
    # we found the solution
    if i.hn == 0:
        pp(i.data)
        print(i.gn)
        n = i.pre
        while n != None:
            pp(n.data)
            print(n.gn)
            n = n.pre
        break
    # find the location of zero
    x,y = dict[i.data.index(0)]
    listNode = i.data
    j = listNode.index(0)
    listNewNode = listNode.copy()
    # based on the location of zero we have options
    # move zero to create a new node
    # move zero up
    if x > 0 :
        listNewNode[j], listNewNode[j - 3] = listNewNode[j - 3] , listNewNode[j]
        # check that the node is new
        for k in array2:
            if k == listNewNode:
                break
        # create the new node
        else:
            newNode = Node(listNewNode,i)
            calFn(newNode)
            array.append(newNode)
            array2.append(newNode.data)
    listNewNode = listNode.copy()
    
    # move zero down
    if x < 2 :
        listNewNode[j], listNewNode[j + 3] = listNewNode[j + 3] , listNewNode[j]
        for k in array2:
            if k == listNewNode:
                break
        else:
            newNode = Node(listNewNode,i)
            calFn(newNode)
            array.append(newNode)
            array2.append(newNode.data)
    listNewNode = listNode.copy()
    
    # move zero left
    if y > 0 :
        listNewNode[j], listNewNode[j - 1] = listNewNode[j - 1] , listNewNode[j]
        for k in array2:
            if k == listNewNode:
                break
        else:
            newNode = Node(listNewNode,i)
            calFn(newNode)
            array.append(newNode)
            array2.append(newNode.data)
    listNewNode = listNode.copy()
    
    # move zero right
    if y < 2 :
        listNewNode[j], listNewNode[j + 1] = listNewNode[j + 1] , listNewNode[j]
        for k in array2:
            if k == listNewNode:
                break
        else:
            newNode = Node(listNewNode,i)
            calFn(newNode)
            array.append(newNode)
            array2.append(newNode.data)
    
    # sort the node based on the f socre
    array = sorted(array, key=lambda x: x.fn)
    
    # for i in array:
    #     print(i.data,i.fn)

print('number of nodes',len(array2))
