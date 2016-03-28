import numpy as np

def isNumber(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def loadNodes(id_value, dictionary, string):
    nodes = []
    #times = []
    file_object = open(string, 'r')
    for line in file_object:
        temp_array = line.split(";")
        if not isNumber(temp_array[0]):
            continue
        if temp_array[1] not in dictionary:
            dictionary[temp_array[1]] = id_value
            id_value += 1
        nodes.append(temp_array[1])
        #times.append(temp_array[3])
    file_object.close()
    return nodes

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
	
def buildMatrix(dictionary, nodes, edges):
    matrix_base = np.zeros((len(dictionary),len(dictionary)))
    absent_nodes = getAbsentNodes(dictionary, nodes)
    size = matrix_base.shape[0]
    for i in range(size):
        for j in range(size):
            if i in absent_nodes or j in absent_nodes:
                matrix_base[i][j] = MIN_VALUE
            for k in range(len(edges)):
                real_i = dictionary[nodes[edges[k][0]]]
                real_j = dictionary[nodes[edges[k][1]]]
                if i == edges[k][0] and j == edges[k][1]:
                    matrix_base[real_i][real_j] = edges[k][2]
                    #matrix_base[real_j][real_i] = edges[k][2]
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
    list_distance = [0 for i in range(len(set_of_graphs))]
    if len(set_of_graphs) == 1:
        return set_of_graphs[0]
    else:
        for i in range(len(set_of_graphs)):
            for j in range(len(set_of_graphs)):
                if i == j:
                    continue
                list_distance[i] += function_distance(set_of_graphs[i], set_of_graphs[j])
        print(list_distance)                
        return set_of_graphs[list_distance.index(min(list_distance))]

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

MIN_VALUE = -100000
dictionary_1 = {}
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
##nodes1 = loadNodes(len(dictionary_1), dictionary_1, "nodesApp.csv")
##nodes2 = loadNodes(len(dictionary_1), dictionary_1, "nodesAll.csv")
##edges1 = loadEdges("edgesApp.csv")
##edges2 = loadEdges("edgesAll.csv")
##mat1 = buildMatrix(dictionary_1, nodes1, edges1)
##mat2 = buildMatrix(dictionary_1, nodes2, edges2)
##mat3 = getmcs(mat1, mat2)


