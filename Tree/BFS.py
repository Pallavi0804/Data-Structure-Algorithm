def bfs(tree,parent,target):
    level = {parent:0}
    visited = {parent:None}
    i = 0
    frontier = [parent]
    while frontier:
        next = []
        for u in frontier:
            for v in tree[u]:
                if v not in level:
                    level[v] = i
                    visited[v] = u
                    next.append(v)
        frontier = next
        i += 1
    path = [target]
    while visited[target] is not None:
        path.insert(0,visited[target])
        target = visited[target]
    return path


tree = {
   "a": ["b", "f"],
   "b": ["a", "c", "g"],
   "c": ["b", "d","l"],
   "d": ["c", "e", "k"],
   "e": ["d", "f"],
   "f": ["a", "e"],
   "g": ["b", "h", "l"],
   "h": ["g", "i"],
   "i": ["h", "j", "k"],
   "j": ["i", "k"],
   "k": ["d", "i", "j", "l"],
   "l": ["c", "g", "k"],
}
parent = "a"
target = "k"
print(bfs(tree,parent,target))
