#!/bin/python3

import sys
from collections import defaultdict

import heapq
import sys

from collections import deque


def search(graph, start, goal):
    visited = {start: None}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = visited[node]
            return path[::-1]
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited[neighbour] = node
                queue.append(neighbour)
    return []

def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count
# G = defaultdict(dict)
G = defaultdict(list)

n, q = input().strip().split(' ')
n, q = [int(n), int(q)]
s = input().strip()
p = input().strip()
for a0 in range(n-1):
    u, v = input().strip().split(' ')
    u, v = [int(u), int(v)]
    # G[u][v] = G[v][u] = 1
    G[u].append(v)
    G[v].append(u)
for a0 in range(q):
    u, v = input().strip().split(' ')
    u, v = [int(u), int(v)]
    # print(u,v)
    L = search(G, u, v)
    S = str()
    # print(L)
    for i in L:
        S += s[i-1]
    print(occurrences(S,p))


# L = search(G, 2,3)
# print(L)
#
# S = str()
# for i in L:
#     S += s[i-1]
# print(S.count(p))
