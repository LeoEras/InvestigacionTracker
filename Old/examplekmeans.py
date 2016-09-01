import numpy as np
import datetime
from random import randint
import random
from math import sqrt
import copy
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def generateCoordenates(minX, maxX, minY, maxY):
    return [random.uniform(minX, maxX), random.uniform(minY, maxY)]

def generateCoordenates2(h, k, r):    
    while True:
        x = random.uniform(h - r, h + r)
        y = random.uniform(k - r, k + r)
        if (((x - h)**2) + ((y - k)**2)) < r**2:
            d = distance([x, y], [h, k])
            value = (1 - d/r)*100
            chance = 0.01*(value - 100)**2
            if random.uniform(0, 100) >= chance:
                return [x, y]
            else:
                return [-1, -1]
            

def getCentroid(set_of_coordinates, function_distance):
    size = len(set_of_coordinates)
    list_distance = [0 for i in range(size)]
    if size == 1:
        return set_of_coordinates[0]
    else:
        for i in range(size):
            for j in range(size):
                if i == j:
                    continue
                list_distance[i] += function_distance(set_of_coordinates[i], set_of_coordinates[j])
        return set_of_coordinates[list_distance.index(min(list_distance))]

def allSame(items):
    return all(x == items[0] for x in items)

def isIsomorph(matrix1, matrix2):
    size = 2
    for i in range(size):
        if matrix1[i] != matrix2[i]:
            return False
    return True

def kmeans(list_of_matrices, clusters, function_distance, mode):
    available = [1 for value in range(clusters)]
    all_used = False
    list_of_median_graphs = [None for value in range(clusters)]
    previous_median_graph_list = []
    membership = [-1 for value in range(len(list_of_matrices))]
    list_of_clusters = [[] for value in range(clusters)]
    list_distances = [0 for value in range(clusters)]
    previous_list = [False for value in range(clusters)]

    if "f" in mode:
        #"Forgy" mode
        #Selecting random items as means of the clusters
        for value in range(clusters):
            selected = randint(0, len(list_of_matrices) - 1)
            while membership[selected] != -1:
                selected = randint(0, len(list_of_matrices))
            membership[selected] = value
            list_of_median_graphs[value] = list_of_matrices[selected]

        #Calculating distances and reassign to clusters
        for index in range(len(list_of_matrices)):
            for value in range(clusters):
                list_distances[value] = function_distance(list_of_matrices[index], list_of_median_graphs[value])

            new_cluster = list_distances.index(min(list_distances))
            list_of_clusters[new_cluster].append(list_of_matrices[index])
            membership[index] = new_cluster
    else:
        #Random mode
        #Assign each item in the list to a random cluster
        for index in range(len(list_of_matrices)):
            rgn = randint(0, clusters - 1)
            availability = available[rgn]
            if not all_used:
                while availability != 1:
                    availability = available[(rgn + 1)%clusters]
                    if availability != 1:
                        rgn = randint(0, clusters - 1)
                        availability = available[rgn]
                    else:
                        rgn = (rgn + 1)%clusters
            membership[index] = rgn
            list_of_clusters[rgn].append(list_of_matrices[index])
            available[rgn] = 0
            all_used = allSame(available)

        #Determining the median of each cluster
        for value in range(clusters):
            list_of_median_graphs[value] = getCentroid(list_of_clusters[value], function_distance)

    while True:
        previous_median_graph_list = copy.deepcopy(list_of_median_graphs)
         
        #Calculating distances and reassign to clusters
        list_of_clusters = [[] for value in range(clusters)]
        for index in range(len(list_of_matrices)):
            for value in range(clusters):
                list_distances[value] = function_distance(list_of_matrices[index], list_of_median_graphs[value])
                
            new_cluster = list_distances.index(min(list_distances))
            list_of_clusters[new_cluster].append(list_of_matrices[index])
            membership[index] = new_cluster

        #Determining the median of each cluster
        for value in range(clusters):
            try:
                list_of_median_graphs[value] = getCentroid(list_of_clusters[value], function_distance)
            except:
                pass
            
        for value in range(clusters):
            previous_list[value] = isIsomorph(previous_median_graph_list[value], list_of_median_graphs[value])

        if any(previous_list):
            break
    return list_of_median_graphs, membership

def distance(coordinate1, coordinate2):
    delta_x = abs(coordinate1[0] - coordinate2[0])
    delta_y = abs(coordinate1[1] - coordinate2[1])
    distance = sqrt(delta_x**2 + delta_y**2)
    return distance

MIN_VALUE = -1
dictionary_1 = {}

start = datetime.datetime.now()

##coor = []
##colors = colors.cnames.keys()
##points = int(raw_input("Points: "))
##num_c = int(raw_input("Clusters: "))
##mode = raw_input("K means mode: ")
##
##o = []
##radius = [0 for value in range(num_c)]
##for i in range(num_c):
##    o.append([randint(0,100), randint(0,100)])
##    radius[i] = randint(1, 10)
##
##for i in range(1, points):
##    for j in range(num_c):
##        if i > j * int(points/num_c) and i <= (j + 1) * int(points/num_c):
####            c = generateCoordenates(randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
##            c = generateCoordenates2(o[j][0], o[j][1], radius[j])
##            while c[0] == -1:
##                c = generateCoordenates2(o[j][0], o[j][1], radius[j])
##            coor.append(c)
##
####o = [randint(0,100), randint(0,100)]
####radius = randint(1, 100)
####
####for i in range(1, points):
######    c = generateCoordenates(0, 100, 0, 100)
####    c = generateCoordenates2(o[0], o[1], radius)
####    while c[0] == -1:
####        c = generateCoordenates2(o[0], o[1], radius)
####    coor.append(c)
####            
##mg, mem = kmeans(coor, num_c, distance, mode)
##
##cx = [[] for item in range(num_c)]
##cy = [[] for item in range(num_c)]
##
##for i in range(points):
##    x = coor[i - 1][0]
##    y = coor[i - 1][1]
##    for w in range(num_c):
##        if mem[i - 1] == w:
##            cx[w].append(x)
##            cy[w].append(y)
##        
##for k in range(num_c):
##    plt.scatter(cx[k], cy[k], color=colors[randint(0, len(colors))])
##
##plt.scatter([mg[k][0] for k in range(num_c)], [mg[k][1] for k in range(num_c)], color="gold")
##plt.show()
##
##coor = []
##colors = colors.cnames.keys()
##points = int(raw_input("Points: "))
##groups = int(raw_input("Groups: "))
##num_c = int(raw_input("Clusters: "))
##mode = raw_input("Mode: ")
##
##o = []
##radius = [0 for value in range(groups)]
##for i in range(groups):
##    o.append([randint(0,100), randint(0,100)])
##    radius[i] = randint(1, 50)
##
##for i in range(points):
##    for j in range(groups):
##        if i > j * int(points/groups) and i <= (j + 1) * int(points/groups):
##            c = generateCoordenates2(o[j][0], o[j][1], radius[j])
##            while c[0] == -1:
##                c = generateCoordenates2(o[j][0], o[j][1], radius[j])
##            coor.append(c)
##
##mg, mem = kmeans(coor, num_c, distance, mode)
##
##cx = [[] for item in range(num_c)]
##cy = [[] for item in range(num_c)]
##
##for i in range(len(coor)):
##    x = coor[i][0]
##    y = coor[i][1]
##    for w in range(num_c):
##        if mem[i] == w:
##            cx[w].append(x)
##            cy[w].append(y)
##        
##for k in range(num_c):
##    plt.scatter(cx[k], cy[k], color=colors[randint(0, len(colors))])
##
##plt.scatter([mg[k][0] for k in range(num_c)], [mg[k][1] for k in range(num_c)], color="gold")
##plt.show()
##
##fig = plt.figure()
##ax = fig.gca()
##fig.show()
##
##x = []
##y = []
##c = []
##coor = []
##colors = colors.cnames.keys()
##ax = fig.add_subplot(111)
##ax.set_xlim([-100, 100])
##ax.set_ylim([-100, 100])
##
##def onclick(event):
##    if event.button != 1:
##        fig.canvas.mpl_disconnect(cid)
##        plt.close()
##    else:
##        for i in range(1, 300):
##            c = generateCoordenates2(event.xdata, event.ydata, 100)
##            while c[0] == -1:
##                c = generateCoordenates2(event.xdata, event.ydata, 100)
##            coor.append(c)
##            x.append(event.xdata)
##            y.append(event.ydata)
##            plt.scatter(c[0], c[1], color="blue")
##        fig.canvas.draw()
##    
##cid = fig.canvas.mpl_connect('button_press_event', onclick)
##plt.show()
##
##num_c = int(raw_input("Clusters: "))
##mode = raw_input("K means mode: ")
##
##for points in range(len(x)):
##    coor.append([x[points], y[points]])
##
##mg, mem = kmeans(coor, num_c, distance, mode)
##
##cx = [[] for item in range(num_c)]
##cy = [[] for item in range(num_c)]
##
##for i in range(len(x)):
##    x = coor[i - 1][0]
##    y = coor[i - 1][1]
##    for w in range(num_c):
##        if mem[i - 1] == w:
##            cx[w].append(x)
##            cy[w].append(y)
##
##for k in range(num_c):
##    plt.scatter(cx[k], cy[k], color=colors[randint(0, len(colors))])
##
##plt.scatter([mg[k][0] for k in range(num_c)], [mg[k][1] for k in range(num_c)], color="gold")
##plt.show()

finish = datetime.datetime.now()
print(finish-start)
