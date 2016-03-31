import numpy as np
import datetime
from random import randint
import copy

def isNumber(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def loadNodes(id_value, dictionary, string):
    nodes = []
    node_size = []
    file_object = open(string, 'r')
    for line in file_object:
        temp_array = line.split(";")
        if not isNumber(temp_array[0]):
            continue
        if temp_array[1] not in dictionary:
            dictionary[temp_array[1]] = id_value
            id_value += 1
        nodes.append(temp_array[1])
        node_size.append(int(temp_array[3]))
    file_object.close()
    return nodes, node_size

def loadEdges(string):
    edges = []
    edge = ()
    file_object = open(string, 'r')
    for line in file_object:
        temp_array = line.split(";")
        if not isNumber(temp_array[0]):
            continue
        edge = (int(temp_array[0]), int(temp_array[1]), int(temp_array[2]))
	#edge = (origin_id, destiny_id, weight)
        edges.append(edge)
    file_object.close()
    return edges

def getAbsentNodes(dictionary, nodes):
    absent_nodes = []
    for item in dictionary:
        if item not in nodes:
            absent_nodes.append(dictionary[item])
    return absent_nodes
	
def buildMatrix(dictionary, nodes, nodes_size, edges):
    matrix_base = np.zeros((len(dictionary),len(dictionary)))
    absent_nodes = getAbsentNodes(dictionary, nodes)
    size = matrix_base.shape[0]
    for i in range(size):
        for j in range(size):
            if i in absent_nodes or j in absent_nodes:
                matrix_base[i][j] = MIN_VALUE
            for k in range(len(edges)):
                #edges[k] is an edge, the k-th edge.
                #edges[k][n] is the n-th element of the k-th edge
                #where n = {0, 1, 2}. 0: Source, 1: Destiny, 2: Weight.
                #Here I look for the edge where i and j appears as source
                #and destiny respectively.
                if i == edges[k][0] and j == edges[k][1]:
                    #Then I look for the node's name. nodes[edges[k][n]].
                    #Finally I look for it's real value in the dictionary of
                    #all the nodes out there. This happens beacause the graph1
                    #doesn't know (and shouldn't really know) graph2's structure
                    real_i = dictionary[nodes[edges[k][0]]]
                    real_j = dictionary[nodes[edges[k][1]]]
                    matrix_base[real_i][real_j] = edges[k][2]
                    #matrix_base[real_j][real_i] = edges[k][2]
    #Loading the weights of the nodes. If there's an arc, it will add with this
    #new value.
    for i in range(size):
        if matrix_base[i][i] != MIN_VALUE:
            if nodes_size:
                matrix_base[i][i] += nodes_size.pop()
    return matrix_base

def getmcs(matrix1, matrix2):
    size = matrix1.shape[0]
    matrix_base = np.ones((size, size))
    matrix_base = np.multiply(MIN_VALUE, matrix_base)
    for i in range(size):
        for j in range(size):
            matrix_base[i][j] = min(matrix1[i][j], matrix2[i][j])
    return matrix_base

def getMCS(matrix1, matrix2):
    size = matrix1.shape[0]
    matrix_base = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            max_val = max(matrix1[i][j], matrix2[i][j])
            if max_val == MIN_VALUE:
                matrix_base[i][j] = 0
            else:
                matrix_base[i][j] = max_val
    return matrix_base

def getSize(matrix):
    size = 0
    num_nodes = matrix.shape[0]
    acum = 0
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i <= j:
                if matrix[i][j] != MIN_VALUE:
                    acum = acum + matrix[i][j]
    invalid_nodes = 0
    for item in matrix[0]:
        if item == -1:
            invalid_nodes += 1
    valid_num_nodes = num_nodes - invalid_nodes
    size = acum + valid_num_nodes
    return float(size)

def getMedianGraph(set_of_graphs, function_distance):
    size = len(set_of_graphs)
    list_distance = [0 for i in range(size)]
    if size == 1:
        return set_of_graphs[0]
    else:
        for i in range(size):
            for j in range(size):
                if i == j:
                    continue
                list_distance[i] += function_distance(set_of_graphs[i], set_of_graphs[j])  
        return set_of_graphs[list_distance.index(min(list_distance))]

def isIsomorph(matrix1, matrix2):
    size = matrix1.shape[0]
    for i in range(size):
        for j in range(size):
            if matrix1[i][j] != matrix2[i][j]:
                return False
    return True

def allSame(items):
    return all(x == items[0] for x in items)

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
            list_of_median_graphs[value] = getMedianGraph(list_of_clusters[value], function_distance)

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
            list_of_median_graphs[value] = getMedianGraph(list_of_clusters[value], function_distance)
            
        for value in range(clusters):
            previous_list[value] = isIsomorph(previous_median_graph_list[value], list_of_median_graphs[value])

        if any(previous_list):
            break
    return list_of_median_graphs, membership

def distanceMCS(matrix1, matrix2):
    return 1 - (getSize(getmcs(matrix1, matrix2))/max(getSize(matrix1), getSize(matrix2)))

def distanceWGU(matrix1, matrix2):
    return 1 - (getSize(getmcs(matrix1, matrix2))/(getSize(matrix1) + getSize(matrix2) - getSize(getmcs(matrix1, matrix2))))
                
def distanceUGU(matrix1, matrix2):
    return getSize(matrix1) + getSize(matrix2) - 2 * getSize(getmcs(matrix1, matrix2))

def distanceMMCS(matrix1, matrix2):
    return getSize(getMCS(matrix1, matrix2)) - getSize(getmcs(matrix1, matrix2))

def distanceMMCSN(matrix1, matrix2):
    return 1 - (getSize(getmcs(matrix1, matrix2))/getSize(getMCS(matrix1, matrix2)))

MIN_VALUE = -1
dictionary_1 = {}

start = datetime.datetime.now()

##nodes1 = loadNodes(len(dictionary_1), dictionary_1, "nt.csv")
##nodes2 = loadNodes(len(dictionary_1), dictionary_1, "nt1.csv")
##nodes2 = loadNodes(len(dictionary_1), dictionary_1, "nodesTest2.csv")
##edges1 = loadEdges("et.csv")
##edges2 = loadEdges("et1.csv")
##edges2 = loadEdges("edgesTest2.csv")
##mat1 = buildMatrix(dictionary_1, nodes1, edges1)
##mat2 = buildMatrix(dictionary_1, nodes2, edges2)
##mat2 = buildMatrix(dictionary_1, nodes2, edges2)
##mat3 = getMCS(mat1, mat2)
##print(getmcs(mat1, mat3))
##print("%.2f" % distanceMCS(mat1, mat2, mat3))
##print(distanceUGU(mat1, mat2, mat3))
##print("Requiero la importancia tambien")
##print("Hay dudas sobre el peso del grafo")
##
##print("Usando distancia MCS")
##print(getMedianGraph([mat1, mat2], distanceMCS))
##print("Usando distancia WGU")
##print(getMedianGraph([mat1, mat2], distanceWGU))
##print("Usando distancia UGU")
##print(getMedianGraph([mat1, mat2], distanceUGU))
##print("Usando distancia MMCS")
##print(getMedianGraph([mat1, mat2], distanceMMCS))
##print("Usando distancia MMCSN")
##print(getMedianGraph([mat1, mat2], distanceMMCSN))
##nodes1, nsize1 = loadNodes(len(dictionary_1), dictionary_1, "nodesApp.csv")
##nodes2, nsize2 = loadNodes(len(dictionary_1), dictionary_1, "nodesAll.csv")
##edges1 = loadEdges("edgesApp.csv")
##edges2 = loadEdges("edgesAll.csv")
##print(sum(nsize2))
##mat1 = buildMatrix(dictionary_1, nodes1, nsize1, edges1)
##mat2 = buildMatrix(dictionary_1, nodes2, nsize2, edges2)
##mat3 = getmcs(mat1, mat2)
##print(getSize(mat2))
##
##nodes = []
##nsizes = []
##edges = []
##matrices = []
##for i in range(1, 9):
##    node, nsize = loadNodes(len(dictionary_1), dictionary_1, "n" + str(i) + ".csv")
##    edge = loadEdges("e" + str(i) + ".csv")
##    nodes.append(node)
##    nsizes.append(nsize)
##    edges.append(edge)
##
##for i in range(1, 9):
##    matrix = buildMatrix(dictionary_1, nodes[i-1], nsizes[i-1], edges[i-1])
##    matrices.append(matrix)
##
##mg, mem = kmeans(matrices, 2, distanceMCS, "r")
##print(mem)
##nodes1, nsize1 = loadNodes(len(dictionary_1), dictionary_1, "nodes_total.csv")
##edges1 = loadEdges("edges_total.csv")
##nodes2, nsize2 = loadNodes(len(dictionary_1), dictionary_1, "nodes_est1.csv")
##edges2 = loadEdges("edges_est1.csv")
##nodes3, nsize3 = loadNodes(len(dictionary_1), dictionary_1, "nodes_est2.csv")
##edges3 = loadEdges("edges_est2.csv")
##mat1 = buildMatrix(dictionary_1, nodes1, nsize1, edges1)
##mat2 = buildMatrix(dictionary_1, nodes2, nsize2, edges2)
##mat3 = buildMatrix(dictionary_1, nodes3, nsize3, edges3)
##
##print("Usando distancia MCS")
##print(distanceMCS(mat1, mat2))
##print(distanceMCS(mat1, mat3))
##
##print("Usando distancia UGU")
##print(distanceUGU(mat1, mat2))
##print(distanceUGU(mat1, mat3))
##
##print("Usando distancia WGU")
##print(distanceWGU(mat1, mat2))
##print(distanceWGU(mat1, mat3))

finish = datetime.datetime.now()
print(finish-start)
