from AdjacencyMatrix import AdjacencyMatrix
class AdjacencyList:
    
#Creating an adjacency list with the number of vertices and the number of lines 
#as variables that can be accessed throughout the class.
    def __init__(self, numberOfVertices, numberOfLines):
        self.numberOfVertices = numberOfVertices
        self.adjacentMatrixList= [[] for i in range(self.numberOfVertices)]
        self.numberOfLines = numberOfLines
  
#Adds an element to the adjacancy list at the vertex and connects the vertex to the connection given.      
    def makeAdjacentElement(self, vertice, connections):
        self.adjacentMatrixList[vertice].append(connections)
        return self.adjacentMatrixList
    
#reads the text from the file that's given
#splits the text from the file into only 2 numbers
#uses the first number as the vertex and the second number as the connection
#calls makeAdjacentElement to put the vertex and connection in the adjacency list
    def readInput(self, file1):
        for x in range(self.numberOfLines):
            line = file1.readline().strip()
            splitLine = line.split()
            vertice = int(splitLine[0])
            connections = int(splitLine[1][0])
            self.makeAdjacentElement(vertice, connections)
            
#Checks to see if the vertex the user has entered is greater than the number of vertex there are in the list
#If it is greater than prints "please choose a valid vertice."
#Else it prints the vertex and the connections that the vertex has.
    def vConnectedto(self, userVertice):
        if(userVertice > self.numberOfVertices):
            print("Please choose a valid vertice. \n")
            return
        else:
            print("The vertice " + str(userVertice) + " is connected to vertice(s) " + str(self.adjacentMatrixList[userVertice]) + ". \n")
        
#Prints the entire graph using a for loop
    def printGraph(self):
        for i in range(self.numberOfVertices - 1):   
            print(str(i + 1) + ": " + str(self.adjacentMatrixList[i + 1] ))
        print("\n")
            
#Checks to see if the vertex the user gave is less than the number of vertices in the list.
#if the user input is greater than the number of vertices, the program prints "Please choose a valid vertice."
#else the new connection is added to the vertex and the original file is updated with the new connection.
    def addConnection(self, newVerticeConnection, new_Connection, file1):
        if(newVerticeConnection > self.numberOfVertices):
            print("Please choose a valid vertice. \n")
            return
        else:
            self.adjacentMatrixList[newVerticeConnection].append(new_Connection)
            file1.write("\n")
            file1.write(str(newVerticeConnection) + " " + str(new_Connection))

#opens a new file called realUserFile
#first writes the number of vertices and goes to a new line
#Next it goes into a for loop writing all of the vertecies and connections into the new file
#finishes by closing the file
    def storeFile(self, realUserFile):
        temp = open(realUserFile, "w+")
        temp.write(str(self.numberOfVertices))
        temp.write("\n")
        for i in range(self.numberOfLines - 1):
            for j in range(len(self.adjacentMatrixList[i])):
                temp.write(str(i) + " " + str(self.adjacentMatrixList[i][j]))
                temp.write("\n")
        temp.close()
        
        
#has two lists created, one for elements visited and the other for where it's supposed to go next.
#start is placed into the queue and the method enters a while loop, as long as the queue isn't empty
#the queue pops the first element and if the node hasn't been put onto the visited list, it's added to the visited list
#Next the method looks at the next element in the matrix and adds it to the queue
#finally, out of the for loop, the list of visited elements is printed.
    def bfs(self, start, matrix):
        if(start > self.numberOfVertices):
            print("Please choose a valid vertice. \n")
        else:
            visited = []
            queue = [start]
            while queue:
                node = queue.pop(0)
                if(node not in visited):
                    visited.append(node)
                    neighbors = matrix[node]
                    for i in neighbors:
                        queue.append(i)
            print(visited)
                
        
#Beings with a stack and a path list
#While there's something in the stack list
#The stack will pop the first element and if it's not in the path list it will be added into it
#The method looks at the next element and adds it to the stack
#out of the for loop, the path list is printed.
    def dfs(self, start, matrix):
        if(start > self.numberOfVertices):
            print("Please choose a valid vertice. \n")
        else:
            stack = [start]
            path = []
            while stack:
                vertex = stack.pop()
                if(vertex not in path):   
                    path.append(vertex)
                    for i in matrix[vertex]:
                        stack.append(i)
            print(path)
        
        
#This is the menu of the function, and it's what you first see when you run the function.
#As long as user doesn't = 7, this menu will conitue to come back to the screen.
#The only thing that's been added to the already exisiting method is asking the user for vertices and connections
#if the function requires it, and a lot of text to help naviagete the program.
    def menu(self, file1, matrix):
        user = -1
        while user != 7:
            print("1. Vertices connected to")
            print("2. Print graph")
            print("3. Add Connection")
            print("4. Store file")
            print("5. BFS")
            print("6. DFS")
            print("7. Exit")
            user = int(input())
            if(user == 1):
                print("Please select a vertice that you wish to see it's connections.")
                print("Please pick a vertices between 1 through " + str(self.numberOfVertices) + ".")
                userVertice = int(input())
                self.vConnectedto(userVertice)
            
            elif(user == 2):
                self.printGraph()
            
            elif(user == 3):
                print("Please tell me the vertice you'd like to add a connection to.")
                newVerticeConnection = int(input())
                print("Please tell me the connection you'd like to add.")
                new_Connection = int(input())
                self.addConnection(newVerticeConnection, new_Connection, file1)
                
            elif(user == 4):
                print("Storing the file.")
                self.storeFile("realUserFile.txt")
                
            elif(user == 5):
                startingNode = int(input("Please give me a starting vertex. \n"))
                self.bfs(startingNode, matrix)
                
            elif(user == 6):
                startingNode = int(input("Please give me a starting vertex. \n"))
                self.dfs(startingNode, matrix)
                
        print("Goodbye!")
        
def main():
#file1 is to read all of the lines of the text and write in changes if there are any
    file1 = open("Numbers.txt", "r+")
#file2 is to find the number of lines of the file.
    file2 = open(r"Numbers.txt")
#Created a matrix to test our two searches
    adjMatrixObj = AdjacencyMatrix(5)
    adjMatrixObj.addEdge(0, 1)
    adjMatrixObj.addEdge(0, 2)
    adjMatrixObj.addEdge(1, 2)
    adjMatrixObj.addEdge(2, 0)
    adjMatrixObj.addEdge(2, 3)
    adjMatrix = adjMatrixObj.getMatrix()
    verticeNumber = int(file1.readline())    
    count = len(file2.readlines()) - 1
    obj = AdjacencyList(verticeNumber, count)
    obj.readInput(file1)
    obj.menu(file1, adjMatrix)
    file1.close()

main()
        
    