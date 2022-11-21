import sys
from enum import Enum

currentPath = []


class Mode(Enum):
    BEST = 1
    FASTEST = 2


nodes = ("liberec", "ceska-lipa", "chrastava",
         "new-york", "turnov", "jablonec-nad-nisou")

graphTime = [
    [999, 999, 12, 24, 22, 20],
    [999, 999, 40, 10, 52, 999],
    [12, 40, 999, 20, 999, 999],
    [24, 10, 20, 999, 15, 30],
    [22, 52, 999, 15, 999, 22],
    [20, 999, 999, 30, 22, 999]
]

graphDistance = [
    [999, 999, 10, 35, 26, 20],
    [999, 999, 47, 30, 67, 999],
    [10, 47, 999, 14, 999, 999],
    [35, 30, 14, 999, 40, 30],
    [26, 67, 999, 40, 999, 24],
    [20, 999, 999, 30, 24, 999]
]

num_of_vertex = len(graphTime[0])
graphTime = [[0 if item == 999 else item for item in row] for row in graphTime]
graphDistance = [[0 if item == 999 else item for item in row]
                 for row in graphDistance]


def getSecondary(first, mode):
    global currentPath
    currentPath = [first] + currentPath
    returnValue = 0
    if (mode == Mode.FASTEST):
        for index, i in enumerate(currentPath):
            if (index == 0):
                continue
            returnValue += graphDistance[i][currentPath[index-1]]
    else:
        for index, i in enumerate(currentPath):
            if (index == 0):
                continue
            returnValue += graphTime[i][currentPath[index-1]]
    return returnValue


def minimumDistance(distance, visited):
    min = 1e11
    min_index = 1e11

    for i in range(num_of_vertex):
        if not visited[i] and distance[i] <= min:
            min = distance[i]
            min_index = i
    return min_index


def appendParentNode(parent, i):
    global currentPath
    if parent[i] == -1:
        return
    appendParentNode(parent, parent[i])
    currentPath.append(i)


def dijkstra(graph, src, target):
    parent = list()
    visited = list()
    distance = list()

    for i in range(num_of_vertex):
        parent.append(-1)
        visited.append(False)
        distance.append(1e11)
    distance[src] = 0
    for i in range(num_of_vertex - 1):
        U = minimumDistance(distance, visited)
        visited[U] = True
        for j in range(num_of_vertex):
            curr_distance = distance[U] + graph[U][j]
            if curr_distance < distance[j] and not visited[j] and graph[U][j]:
                parent[j] = U
                distance[j] = curr_distance
    return (distance[target], parent)


for line in sys.stdin:
    line = line.rstrip().split(" ")
    if (line[2] == 'nejkratsi'):
        method = Mode.FASTEST
    else:
        method = Mode.BEST

    source = nodes.index(line[0])
    target = nodes.index(line[1])

    currentPath = []
    if (method == Mode.BEST):
        (result, parent) = dijkstra(graphTime, source, target)
        appendParentNode(parent, target)
        secondaryResult = getSecondary(source, Mode.FASTEST)
        print("({} min, {} km) {}".format(
            result, secondaryResult, nodes[source]), end="")
    else:
        (result, parent) = dijkstra(graphDistance, source, target)
        appendParentNode(parent, target)
        secondaryResult = getSecondary(source, Mode.BEST)
        print("({} min, {} km) {}".format(
            secondaryResult, result, nodes[source]), end="")
    for index, i in enumerate(currentPath):
        if (index == 0):
            continue
        print(" -> {}".format(nodes[i]), end="")
    print("")
