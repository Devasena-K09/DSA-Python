from collections import deque

graph = {
    0: [1, 2],
    1: [3],
    2: [],
    3: []
}

def bfs(start):

    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:

        node = queue.popleft()

        print(node, end=" ")

        for neighbor in graph[node]:

            if neighbor not in visited:

                visited.add(neighbor)
                queue.append(neighbor)

bfs(0)
