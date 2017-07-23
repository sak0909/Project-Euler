#!/bin/python3

import sys
from collections import defaultdict
from collections import Counter
from collections import deque
from heapq import heappush, heappop
from queue import PriorityQueue
import functools
import math
from math import sqrt

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.all_distance = defaultdict(list)
        self.costs = []
        self.ans = 0
        self.distance = [-1] * (self.V + 1)
        self.parent = [-1 for i in range(self.V + 1)]

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def setCosts(self, c):
        self.costs = [0]+ c

    def findShortestDistance(self, s, e):
        visited = [False] * (self.V + 1)

        Q = deque()
        Q.append(s)

        visited[s] = True
        while len(Q):
            u = Q.popleft()
            if u in self.graph:
                for v in self.graph[u]:
                    if not visited[v]:
                        self.parent[v] = u
                        visited[v] = True
                        if v == e:
                            break
                        if v in self.graph:
                            Q.append(v)
        values = []
        u = e
        while u != s:
            values.append(self.costs[u])
            u = self.parent[u]
        values.append(self.costs[u])

        return values


if __name__ == "__main__":
    n, q = input().strip().split(' ')
    n, q = [int(n), int(q)]
    c = list(map(int, input().strip().split(' ')))
    G = Graph(n)
    G.setCosts(c)
    for a0 in range(n-1):
        u, v = input().strip().split(' ')
        u, v = [int(u), int(v)]
        G.addEdge(u, v)
    for a0 in range(q):
        u, v, K = input().strip().split(' ')
        u, v, K = [int(u), int(v), int(K)]
        values = G.findShortestDistance(u , v)
        freq = Counter(values)
        l = sorted([(j,i) for i,j in freq.items()], reverse=True)

        print(l[K-1][1])
