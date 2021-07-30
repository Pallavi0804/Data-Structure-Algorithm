# first step take graph as input
from collections import defaultdict
def dfs(graph, start, visited, path):
    path.append(start)
    visited[start] = True
    for neighbour in graph[start]:
        if visited[neighbour] == False:
            dfs(graph, neighbour, visited, path)
    return path

# drivers code
path = []
start = "A"
visited = defaultdict(bool)
v, e = map(int, input().split())  # taking no vertices and edges as input
graph = defaultdict(list)
level = 0
for i in range(e):
    u, v = map(str, input().split())
    graph[u].append(v)
    graph[v].append(u)
print("Graph ",graph)
traversedPath = dfs(graph, start, visited, path)
print(traversedPath)

'''input
7 9
A B
A C
A F
C E
C F
C D
D E
D G
G F
-----
7 6
A B
A C
A F
C E
C D
G F
'''
