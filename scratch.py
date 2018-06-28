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
<<<<<<< 4d29a0f01026d8ceccdb7ad1633a966ba39322ef
=======

class OfflineLCA(defaultdict):
    """Find LCAs of all pairs in a given sequence, using Union-Find."""

    def __init__(self,parent,pairs):
        """Set up to find LCAs of pairs in tree defined by parent.
        LCA of any given pair x,y can then be found by self[x][y].
        However unlike the online LCA structure we can not find LCAs
        of pairs that are not supplied to us at startup time.
        """

        # set up dictionary where answers get stored
        defaultdict.__init__(self,dict)
        for u,v in pairs:
            self[u][v] = self[v][u] = None

        # set up data structure for finding node ancestor on search path
        # self.descendants forms a collection of disjoint sets,
        #    one set for the descendants of each search path node.
        # self.ancestors maps disjoint set ids to the ancestors themselves.
        self.descendants = UnionFind()
        self.ancestors = {}

        # invert the parent relationship so we can traverse the tree
        self.children = defaultdict(list)
        for x,px in parent.items():
            self.children[px].append(x)
        root = [x for x in self.children if x not in parent]
        if len(root) != 1:
            raise ValueError("LCA input is not a tree")

        # initiate depth first traversal
        self.visited = set()
        self.traverse(root[0])

    def traverse(self,node):
        """Perform depth first traversal of tree."""
        self.ancestors[self.descendants[node]] = node
        for child in self.children[node]:
            self.traverse(child)
            self.descendants.union(child,node)
            self.ancestors[self.descendants[node]] = node
        self.visited.add(node)
        for query in self[node]:
            if query in self.visited:
                lca = self.ancestors[self.descendants[query]]
                self[node][query] = self[query][node] = lca
>>>>>>> new stuff

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.all_distance = defaultdict(list)
<<<<<<< 4d29a0f01026d8ceccdb7ad1633a966ba39322ef
        self.costs = []
        self.ans = 0
        self.distance = [-1] * (self.V + 1)
        self.parent = [-1 for i in range(self.V + 1)]
=======
        # self.visited = [False] * (vertices + 1)
        self.costs = []
        self.fib = {0:1, 1:1}
        self.ans = 0

        # for i in range(vertices+1):
        #     self.all_distance[i] = [-1] * (vertices + 1)

    def get_fib(self, n):
        if n in self.fib:
            return self.fib[n]
        else:
            self.fib[n] = (self.get_fib(n-1)%1000000007 + self.get_fib(n-2)%1000000007) %1000000007
            return self.fib[n]
>>>>>>> new stuff

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def setCosts(self, c):
        self.costs = [0]+ c

<<<<<<< 4d29a0f01026d8ceccdb7ad1633a966ba39322ef
    def findShortestDistance(self, s, e):
=======
    def findShortestDistance(self, s):
        distance = [-1] * (self.V + 1)
        distance[s] = self.costs[s]
>>>>>>> new stuff
        visited = [False] * (self.V + 1)

        Q = deque()
        Q.append(s)

        visited[s] = True
        while len(Q):
            u = Q.popleft()
<<<<<<< 4d29a0f01026d8ceccdb7ad1633a966ba39322ef
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
=======
            d = distance[u]
            if u in self.graph:
                for v in self.graph[u]:
                    if (not visited[v]):
                        distance[v] = d + self.costs[v]
                        visited[v] = True
                        if v in self.graph:
                            Q.append(v)

        # self.all_distance[s] = distance
        self.ans = (self.ans + sum([self.get_fib(i) %1000000007 for i in distance[1:]]))%1000000007
        # print(distance)

    def findShortestDistanceForAll(self):
        for i in range(1, self.V + 1):
            self.findShortestDistance(i)
        # print(self.all_distance)

    def printAnswer(self):
        ans = 0
        for i in range(1, self.V + 1):
            for j in range(1, self.V + 1):
                self.all_distance[i][j] = self.get_fib(self.all_distance[i][j])
                ans = (ans + self.all_distance[i][j]) %1000000007
        print(ans)

if __name__ == "__main__":
    n = int(input().strip())
    G = Graph(n)
    for _ in range(n-1):
        u,v = list(map(int,input().strip().split(' ')))
        G.addEdge(u,v)
    costs = list(map(int,input().strip().split(' ')))
    G.setCosts(costs)
    G.findShortestDistanceForAll()
    # G.printAnswer()
    print(G.ans)
>>>>>>> new stuff
