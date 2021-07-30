from collections import defaultdict
def dfs(tree,source,visited,path,level,i):
    path.append(source)
    visited[source] = True
    level[source] = i + 1
    i+=1
    for neighbour in tree[source]:
        if visited[neighbour] is False:
            dfs(tree,neighbour,visited,path,level,i)
    return path,level

# Taking Input
tree = defaultdict(list)
v, e = map(int, input().split())  # Taking no. of vertices and edges as input
for i in range(e):
    u, v = map(str, input().split())
    tree[u].append(v)
    tree[v].append(u)
source = "A"
visited = defaultdict(bool)
path = []
level={}
i = 0
level[source] = i
print("Traversed Path and Level of each vertex")
print(dfs(tree, source,visited, path,level,i))

'''input
7 6
1 2 
1 3
1 4
3 5
3 6
4 7
----
7 6
A B
A C
A F
C E
C D
G F
'''
