from collections import deque

def topological_sort(graph):

    indegree = {
        node: 0
        for node in graph
    }

    for node in graph:

        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = deque(
        [
            node
            for node in indegree
            if indegree[node] == 0
        ]
    )

    result = []

    while queue:

        node = queue.popleft()

        result.append(node)

        for neighbor in graph[node]:

            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result


graph = {
    0:[1,2],
    1:[3],
    2:[3],
    3:[]
}

print(topological_sort(graph))
