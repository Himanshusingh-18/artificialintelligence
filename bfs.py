from collections import deque

# Sample graph implemented as a dictionary
graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

# Implement Logic of BFS
def bfs(start):
    queue = deque([start])
    levels = {start: 0}  # This Dict Keeps track of levels
    visited = set([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                levels[neighbor] = levels[node] + 1

    print(levels)  # print graph level
    return visited

print(str(bfs('A')))  # print graph node

# For Finding Breadth First Search Path
def bfs_paths(graph, start, goal):
    queue = deque([(start, [start])])

    while queue:
        vertex, path = queue.popleft()

        for next_vertex in graph[vertex] - set(path):
            if next_vertex == goal:
                yield path + [next_vertex]
            else:
                queue.append((next_vertex, path + [next_vertex]))

result = list(bfs_paths(graph, 'A', 'F'))
print(result)  # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

# For finding the shortest path
def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

result1 = shortest_path(graph, 'A', 'F')
print(result1)  # ['A', 'C', 'F']


