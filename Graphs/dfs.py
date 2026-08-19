graph = {
    0: [1, 2],
    1: [3],
    2: [],
    3: []
}

visited = set()

def dfs(node):

    if node in visited:
        return

    visited.add(node)

    print(node, end=" ")

    for neighbor in graph[node]:
        dfs(neighbor)

dfs(0)
