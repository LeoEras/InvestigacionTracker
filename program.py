from myTree import *
import numpy as np
from random import randint
import random
import time

def createTable(rows, cols):
    table = np.zeros((rows, cols))
    return table

def createNodes(table, nodes):
    rows = table.shape[0]
    cols = table.shape[1]
    for i in range(rows):
        for j in range(cols):
            node = Node(i, j)
            node.setValue(0)
            nodes.append(node)

def joinNodes(table, nodes):
    rows = int(table.shape[0])
    cols = int(table.shape[1])
    counter = 0
    for k in range(len(nodes)):
        real_i = k/rows
        real_j = k % cols
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    if (real_i + i) > -1 and (real_i + i) < rows and (real_j + j) > -1 and (real_j + j) < cols:
                        nodes[k].connect(nodes[(real_i + i)*rows + (real_j + j)])

def buildTree(node, table, nodes, val):
    rows = int(table.shape[0])
    cols = int(table.shape[1])
    actual = node
    if actual.value > 0:
        return 
    else:
        actual.value = val
    real_i = actual.posX
    real_j = actual.posY
    table[real_i][real_j] = val
    for i in range(-2, 3):
        for j in range(-2, 3):
            if i == j and (i > -2 and i < 2 and j > -2 and j < 2) and (i == 0 or j == 0):
                continue
            else:
                if (real_i + i) > -1 and (real_i + i) < rows and (real_j + j) > -1 and (real_j + j) < cols:
                    actual.connect(nodes[(real_i + i)*rows + (real_j + j)])
                    val += 1
                    table[real_i + i][real_j + j] == val

    for item in actual.edges:
        buildTree(item, table, nodes, val)
                
    return table

def completeTable(table, i, j, value):
    rows = int(table.shape[0])
    cols = int(table.shape[1])

    index = np.argmax(table)
    if index == len(table):
        return

    print(table)
    if table[i][j] == 0:
        table[i][j] = value
        new_i, new_j = randomPosition(i, j)
        while (new_i < 0 or new_j < 0 or new_i >= rows or new_j >= cols):
            new_i, new_j = randomPosition(i, j)

        completeTable(table, new_i, new_j, value + 1)
    else:
        print("ERROR")
        index = np.argmax(table)
        real_i = index / cols
        real_j = index % cols
        print(real_i, real_j, index)
        temp = table[real_i][real_j]
        print(temp)
        new_i, new_j = randomPosition(real_i, real_j)
        while (new_i < 0 or new_j < 0 or new_i >= rows or new_j >= cols):
            new_i, new_j = randomPosition(real_i, real_j)

        completeTable(table, new_i, new_j, temp + 1)

def randomPosition(i, j):
    rnd = randint(-2,2)
    while rnd == 0:
        rnd = randint(-2,2)
    new_i = i + rnd
    if rnd == -1 or rnd == 1:
        new_j = j + random.choice([-2, 2])
    if rnd == -2 or rnd == 2:
        new_j = j + random.choice([-1, 1])
    return new_i, new_j
        
    
    
table = createTable(4, 3)
nodes = []
createNodes(table, nodes)
completeTable(table, 1, 0, 1)
print(table)


