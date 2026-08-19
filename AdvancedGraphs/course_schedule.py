from collections import defaultdict

def can_finish(num_courses, prerequisites):

    graph = defaultdict(list)

    for course, prereq in prerequisites:
        graph[course].append(prereq)

    visiting = set()
    visited = set()

    def dfs(course):

        if course in visiting:
            return False

        if course in visited:
            return True

        visiting.add(course)

        for prereq in graph[course]:

            if not dfs(prereq):
                return False

        visiting.remove(course)
        visited.add(course)

        return True

    for course in range(num_courses):

        if not dfs(course):
            return False

    return True


print(can_finish(
    2,
    [[1,0]]
))
