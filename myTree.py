class Node(object):
    def __init__(self, dataX, dataY):
        self.posX = dataX
        self.posY = dataY
        self.value = 0
        self.edges = []

    def connect(self, obj):
        self.edges.append(obj)

    def setValue(self, val):
        self.value = val
