from collections import deque

def shortest_path(graph, start, end):

    queue = deque(
        [(start, 0)]
    )

    visited = {start}

    while queue:

        node, distance = queue.popleft()

        if node == end:
            return distance

        for neighbor in graph[node]:

            if neighbor not in visited:

                visited.add(neighbor)

                queue.append(
                    (neighbor, distance + 1)
                )

    return -1


graph = {
    0:[1,2],
    1:[3],
    2:[3],
    3:[]
}

print(
    shortest_path(
        graph,
        0,
        3
    )
)
