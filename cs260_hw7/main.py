"""
Author: Kenny Choi
Assignment 7
5/27/18

"""

def graph(file):  # returns adjacency matrix representation
    with open(file, "r") as f:
        lines = [x.strip() for x in f]
        dimension = int(lines[0])
        edges = lines[1:]

        adjMatrix = [[0 for x in range(dimension)] for y in range(dimension)]  # initialize matrix
        for i in edges:
            a, b, e = [int(x) for x in i.split()]
            adjMatrix[a][b] = e
            adjMatrix[b][a] = e

    return adjMatrix


def sortedGraph(file):
    sortedGraph = dict()
    sortedEdges = []
    with open(file, "r") as f:
        lines = [x.strip() for x in f]
        vertexes = lines[0]
        edges = lines[1:]
        for i in edges:
            a, b, e = [int(x) for x in i.split()]
            sortedEdges.append((str(a), str(b), e))
        sortedEdges.sort(key=lambda x: x[2])
        listVertexes= list(range(int(vertexes)))
        for i in listVertexes:
            listVertexes[i] = str(i)
        sortedGraph["V"] = listVertexes
        sortedGraph["E"] = set(sortedEdges)
        return sortedGraph


def prim(G, start_node):  # G should be adjacency matrix representation
    v = list(range(len(G)))
    u = [start_node]
    knownEdges = []
    currentNode = start_node
    print("Starting Node:", start_node)

    while u != v:
        oldRow = G[currentNode]  # complete destinations from current node
        newRow = list(filter(lambda x: x != 0, oldRow))  # available destinations from current node

        for i in newRow:
            knownEdges.append([currentNode, oldRow.index(i), i])  # [src, dst, dist]
        knownEdges.sort(key=lambda x: x[2])  # sort by distances
        while True:
            node = knownEdges.pop(0)
            currentNode = node[0]
            nextNode = node[1]

            if nextNode not in u:
                u.append(nextNode)
                break
            elif knownEdges == []:
                break
            else:
                continue
        u.sort()
        a = currentNode
        b = nextNode
        print("Added", nextNode)
        if a < b:
            print("Using Edge [{0:d}, {1:d}, {2:.1f}]".format(a, b, G[a][b]))
        else:
            print("Using Edge [{0:d}, {1:d}, {2:.1f}]".format(b, a, G[a][b]))
        currentNode = nextNode


dict1 = dict()
dict2 = dict()


def make_set(vertex):
    dict1[vertex] = vertex
    dict2[vertex] = 0


def find(vertex):
    if dict1[vertex] != vertex:
        dict1[vertex] = find(dict1[vertex])
    return dict1[vertex]


def union(vertex1, vertex2):
    root1 = find(vertex1)
    root2 = find(vertex2)
    if root1 != root2:
        if dict2[root1] > dict2[root2]:
            dict1[root2] = root1
        else:
            dict1[root1] = root2
        if dict2[root1] == dict2[root2]:
            dict2[root2] += 1


def kruskal(G):
    mst = []
    edges = list(G['E'])
    edges.sort(key=lambda x: x[2])

    for vertex in G['V']:
        make_set(vertex)

    for edge in edges:
        vertex1, vertex2, weight = edge
        if find(vertex1) != find(vertex2):
            union(vertex1, vertex2)
            mst.append(edge)

    for i in mst:
        if int(i[0]) > int(i[1]):
            a = int(i[1])
            b = int(i[0])
        else:
            a = int(i[0])
            b = int(i[1])
        print("Select Edge: [{0:d}, {1:d}, {2:.1f}]".format(a, b, i[2]))

def help():
    print("Commands:")
    print("exit or ctrl-d - quits the program")
    print("help - prints this menu")
    print("prim integer_value - runs Prim's algorithm starting at node given")
    print("kruskal - runs Kruskal's algorithm")

if __name__ == "__main__":
    print("Welcome to Minimum Spanning Tree Finder")
    filename = input("Give the file name graph is in: ")
    graph = graph(filename)
    help()
    while True:
        userInput = input("Enter command: ")
        userInput = userInput.split()
        if userInput[0] == "prim":
            print("Running Prim's Algorithm")
            prim(graph, int(userInput[1]))
        elif userInput[0] == "kruskal":
            print("Running Kruskal's Algorithm")
            kruskal(sortedGraph(filename))
        elif userInput[0] == "help":
            help()
        elif userInput[0] == "exit":
            print("Bye")
            break
        else:
            print("invalid entry")