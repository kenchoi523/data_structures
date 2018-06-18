"""
Author: Kenny Choi
Assignment 8
6/3/18

"""
import queue
import math


def listEdges(file):
    with open(file, "r") as f:
        lines = [x.strip() for x in f]
        dimension = int(lines[0])
        edges = lines[1:]
        listEdges = []
        for i in edges:
            a, b, e = [int(x) for x in i.split()]
            listEdges.append([a,b,e])
    return listEdges, dimension


def adjMatrix(file):  # returns adjacency matrix representation
    with open(file, "r") as f:
        lines = [x.strip() for x in f]
        dimension = int(lines[0])
        edges = lines[1:]

        adjMatrix = [[math.inf for x in range(dimension)] for y in range(dimension)]  # initialize matrix
        for i in edges:
            a, b, e = [int(x) for x in i.split()]
            adjMatrix[a][b] = float(e)
        for i in range(dimension):
            adjMatrix[i][i] = 0.0
    return adjMatrix


def weight(G, u, v):
    for i in range(len(G)):
        if G[i][0] == u and G[i][1] == v:
            return G[i][2]
    return math.inf


def dijkstra(G, a):
    d = [math.inf for x in range(numNodes)]
    d[a] = 0
    Q = queue.PriorityQueue()
    Q.put(a)
    while not Q.empty():
        u = Q.get()
        adjNodes = []
        for i in range(len(G)):
            if G[i][0] == u:
                adjNodes.append(G[i][1])
        for v in adjNodes:
            if d[v] == math.inf:
                d[v] = d[u] + weight(G, u, v)
                Q.put(v)
            if d[v] > d[u] + weight(G, u, v):
                d[v] = d[u] + weight(G, u, v)
                Q.put(v)
    for i in range(len(d)):
        if d[i] != math.inf:
            d[i] = float(d[i])
    return d


def floyd(G):
    A = G
    for k in range(numNodes):
        for i in range(numNodes):
            for j in range(numNodes):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
    return A


def help():
    print("Possible Commands are:")
    print("dijkstra x - Runs Dijkstra starting at node X. X must be an integer")
    print("floyd - Runs Floyd's algorithm")
    print("help - prints this menu")
    print("exit or ctrl-D - Exits the program")



if __name__ == "__main__":
    edges, numNodes = listEdges("input1.txt")
    graph = adjMatrix("input1.txt")

    f = floyd(graph)


    filename = input("File containing graph: ")
    graph = adjMatrix(filename)
    edges, numNodes = listEdges(filename)
    help()
    while True:
        userInput = input("Enter command: ")
        userInput = userInput.split()
        if userInput[0] == "dijkstra":
            d = dijkstra(edges, int(userInput[1]))
            print(d)
        elif userInput[0] == "floyd":
            f = floyd(graph)
            for i in f:
                print(i)
        elif userInput[0] == "help":
            help()
        elif userInput[0] == "exit":
            print("Bye")
            break
        else:
            print("invalid entry")