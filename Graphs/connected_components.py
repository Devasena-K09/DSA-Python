def dfs(node, graph, visited):

    visited.add(node)

    for neighbor in graph[node]:

        if neighbor not in visited:
            dfs(neighbor, graph, visited)


def count_components(graph):

    visited = set()
    count = 0

    for node in graph:

        if node not in visited:

            dfs(node, graph, visited)
            count += 1

    return count
