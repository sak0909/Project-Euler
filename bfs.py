__author__ = 'Sak'

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.parent = [i for i in range(self.V + 1)]

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    def findShortestDistance(self, s, e):
        '''
        Returns the shortest path from s to e using BFS
        '''
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
        path = []
        u = e
        while u != s:
            path.append(u)
            u = self.parent[u]
        path.append(u)

        return path[::-1]
