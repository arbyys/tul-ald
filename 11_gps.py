
import json
import sys
from enum import Enum


class Method(Enum):
    FASTEST = 1
    SHORTEST = 2


nodes = ("liberec", "ceska-lipa", "chrastava",
         "new-york", "turnov", "jablonec-nad-nisou")

times = [
    [999, 999, 12, 24, 22, 20],
    [999, 999, 40, 10, 52, 999],
    [12, 40, 999, 20, 999, 999],
    [24, 10, 20, 999, 15, 30],
    [22, 52, 999, 15, 999, 22],
    [20, 999, 999, 30, 22, 999]

]

cityDistances = [
    [999, 999, 10, 35, 26, 20],
    [999, 999, 47, 30, 67, 999],
    [10, 47, 999, 14, 999, 999],
    [35, 30, 14, 999, 40, 30],
    [26, 67, 999, 40, 999, 24],
    [20, 999, 999, 30, 24, 999]
]

nodeDistances = {}
nodeDistances2 = {}

for i in range(len(nodes)):
    for j in range(len(nodes)):
        if (j == i):
            continue
        time = times[i][j]
        if (time == 999):
            continue
        if (nodes[i] not in nodeDistances):
            nodeDistances[nodes[i]] = {}
        nodeDistances[nodes[i]][nodes[j]] = time

for i in range(len(nodes)):
    for j in range(len(nodes)):
        if (j == i):
            continue
        time = cityDistances[i][j]
        if (time == 999):
            continue
        if (nodes[i] not in nodeDistances2):
            nodeDistances2[nodes[i]] = {}
        nodeDistances2[nodes[i]][nodes[j]] = time


class Dijkstra:

    def __init__(self, vertices, method):
        self.vertices = vertices  # ("A", "B", "C" ...)
        if (method == Method.FASTEST):
            self.graph = nodeDistances
            self.graph2 = nodeDistances2
        else:
            self.graph = nodeDistances2
            self.graph2 = nodeDistances

    def find_route(self, start, end):
        unvisited = {n: float("inf") for n in self.vertices}
        unvisited2 = {n: float("inf") for n in self.vertices}
        unvisited[start] = 0  # set start vertex to 0
        unvisited2[start] = 0  # set start vertex to 0
        visited = {}  # list of all visited nodes
        visited2 = {}  # list of all visited nodes
        parents = {}  # predecessors
        parents2 = {}  # predecessors

        while unvisited:
            # get smallest distance
            min_vertex = min(unvisited, key=unvisited.get)
            for neighbour, _ in self.graph.get(min_vertex, {}).items():
                if neighbour in visited:
                    continue
                new_distance = unvisited[min_vertex] + \
                    self.graph[min_vertex].get(neighbour, float("inf"))
                if new_distance < unvisited[neighbour]:
                    unvisited[neighbour] = new_distance
                    parents[neighbour] = min_vertex
            visited[min_vertex] = unvisited[min_vertex]
            visited2[min_vertex] = unvisited2[min_vertex]
            unvisited.pop(min_vertex)

            if min_vertex == end:
                break

        while unvisited2:
            min_vertex = min(unvisited2, key=unvisited2.get)
            for neighbour, _ in self.graph2.get(min_vertex, {}).items():
                if neighbour in visited2:
                    continue
                new_distance = unvisited2[min_vertex] + \
                    self.graph2[min_vertex].get(neighbour, float("inf"))
                if new_distance < unvisited2[neighbour]:
                    unvisited2[neighbour] = new_distance
                    parents2[neighbour] = min_vertex

            visited2[min_vertex] = unvisited2[min_vertex]
            unvisited2.pop(min_vertex)
            if min_vertex == end:
                break
        return (parents, visited, visited2)

    @staticmethod
    def generate_path(parents, start, end):
        path = [end]
        while True:
            key = parents[path[0]]
            path.insert(0, key)
            if key == start:
                break
        return path


def getPath(method: Enum, start, end):

    d = Dijkstra(nodes, method)

    if (method == Method.FASTEST):
        p, v, v2 = d.find_route(start, end)
    else:
        p, v2, v = d.find_route(start, end)

    se = d.generate_path(p, start, end)
    return (v, v2, se)


for line in sys.stdin:
    line = line.rstrip().split(" ")
    if (line[2] == 'nejkratsi'):
        method = Method.SHORTEST
    else:
        method = Method.FASTEST

    v, v2, se = getPath(method, line[0], line[1])

    print(v)
    print(v2)

    print("({} min, {} km) {}".format(
        list(v.values())[-1], list(v2.values())[-1], " -> ".join(se)))
