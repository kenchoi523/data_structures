import sys
import queue

def adjacentNodes(G, node):
    toNodes = []
    for i in range(0, len(G)):
        if G[i][0] == node:
            toNodes.append(G[i][1])
    return toNodes

def getWeight(G, fromNode, toNode):
    for i in range(0, len(G)):
        if G[i][0] == fromNode and G[i][1] == toNode:
            return G[i][2]
    return float("inf")

def dijkstra(G, start_node):
    distance = [None]*num_Nodes
    for i in nodes:
        distance[i] = float("inf")
    distance[start_node] = 0.0
    pq = queue.PriorityQueue()
    pq.put(start_node)
    while not pq.empty():
        currentNode = pq.get()
        for nextNode in adjacentNodes(G, currentNode):
            newDistance = distance[currentNode] + getWeight(G, currentNode, nextNode)
            if distance[nextNode] == float("inf"):
                distance[nextNode] = newDistance
                pq.put(nextNode)
            if distance[nextNode] > newDistance:
                distance[nextNode] = newDistance
                pq.put(nextNode)
    return distance


def reArrangeMatrix(G):
    newMatrix = [None]*num_Nodes
    distancesFromNode = [None]*num_Nodes
    
    for fromNode in range(0, num_Nodes):
        for toNode in range(0, num_Nodes):
            if toNode == fromNode:
                distancesFromNode[fromNode] = 0.0
            else:
                distancesFromNode[toNode] = getWeight(G, fromNode, toNode)
        newMatrix[fromNode] = distancesFromNode
        distancesFromNode = [None]*num_Nodes
    return newMatrix
        
def printSolution(newMatrix):
    for i in range(0, num_Nodes):
        print(newMatrix[i])

def floyd(G):
    newMatrix = reArrangeMatrix(G)

    for k in range(0, num_Nodes):
        for i in range(0, num_Nodes):
            for j in range(0, num_Nodes):
                newMatrix[i][j] = min(newMatrix[i][j], newMatrix[i][k] + newMatrix[k][j])
    return newMatrix


fileName = input("File containing graph: ")
txt = open(fileName, 'r')
num_Nodes = int(txt.readline().split(" ")[0])
matrix = []
nodes = []

while True:
    line = txt.readline().split(" ") 
    if line[0] == '':
        break
    fromNode = int(line[0])
    if fromNode not in nodes:
        nodes.append(fromNode)
    toNode   = int(line[1])
    weight   = float(line[2])
    lineArray = [fromNode, toNode, weight]
    matrix.append(lineArray)

print("Possible Commands are: ")
print("dijkstra x - Runs Dijkstra starting at node X. X must be an integer")
print("floyd - Runs Floyd's algorithm")
print("help - prints this menu")
print("exit or ctrl-D - Exits the program")

command = input("Enter command: ")

while command != "exit":
    if command == "help":
        print("Possible Commands are: ")
        print("dijkstra x - Runs Dijkstra starting at node X. X must be an integer")
        print("floyd - Runs Floyd's algorithm")
        print("help - prints this menu")
        print("exit or ctrl-D - Exits the program")
        command = input("Enter command: ")
    elif command.split(" ")[0] == "dijkstra":
        start_node = int(command.split(" ")[1])
        print(dijkstra(matrix, start_node))
        command = input("Enter command: ")
    elif command == "floyd":
        printSolution(floyd(matrix))
        command = input("Enter command: ")

print("Bye")

