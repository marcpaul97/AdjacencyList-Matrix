
class AdjacencyMatrix:
#Making a very simple matrix to test out our two searches
#The matrix and the size of the matrix are the only variables that can be used throughout this class.
    def __init__(self, size):
        self.adjacencyMatrix = []
        for i in range(size):
            self.adjacencyMatrix.append([0 for i in range(size)])
        self.size = size
        
        
#This method adds a vertex if the two vertice's are different
    def addEdge(self, vertice, vertice2):
        if(vertice == vertice2):
            print("These are the same vertex.")
        self.adjacencyMatrix[vertice][vertice2] = 1
        self.adjacencyMatrix[vertice2][vertice] = 1
        
#Checks to see if the vertices in the matrix are 0
#if they are, the programs job is done.
#if it isn't it sets both vertices = 0
    def removeEdge(self, vertice, vertice2):
        if(self.adjacencyMatrix[vertice][vertice2] == 0):
            print("There isn't an edge between these vertices.")
            return
        self.adjacencyMatrix[vertice][vertice2] = 0
        self.adjacencyMatrix[vertice2][vertice] = 0
        
        
#a simple function seeing if the an edge is in the current matrix
    def containsEdge(self, vertice, vertice2):
        if(self.adjacencyMatrix[vertice][vertice2] > 0):
            return True
        return False
    
#returns the length of the matrix
    def getLength(self):
        return self.size
    
#A way to view the entire matrix if we ever need to print it
#Formats the matrix so each number takes up 3 spaces to make it look cleaner
    def printMatrix(self):
        for row in self.adjacencyMatrix:
            for element in row:
                print('{:3}'.format(element)),
            print
            
#returns the matrix
    def getMatrix(self):
        return self.adjacencyMatrix