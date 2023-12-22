import matplotlib.pyplot as plt

# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

# Depth-limited search algorithm
def depth_limited_search(graph, source, destination, limit):
    visited = set()
    path = []

    def dfs(node, depth):
        visited.add(node)
        path.append(node)

        if node == destination:
            return True

        if depth == limit:
            path.pop()
            return False

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, depth + 1):
                    return True

        path.pop()
        return False

    if dfs(source, 0):
        return path
    else:
        return None

# Run depth-limited search
source = 'A'
destination = 'H'
limit = 3
found_path = depth_limited_search(graph, source, destination, limit)

# Visualize the graph and highlight the found path
def visualize_graph(graph, found_path):
    pos = {
        'A': (0, 0),
        'B': (1, 1),
        'C': (1, -1),
        'D': (2, 2),
        'E': (2, 0),
        'F': (2, -2),
        'G': (3, -1),
        'H': (3, 1)
    }

    plt.figure(figsize=(6, 6))
    plt.axis('off')

    for node in graph:
        for neighbor in graph[node]:
            plt.plot([pos[node][0], pos[neighbor][0]], [pos[node][1], pos[neighbor][1]], 'k-')

    for node in graph:
        plt.text(pos[node][0], pos[node][1], node, ha='center', va='center', fontsize=12, fontweight='bold')

    if found_path:
        for i in range(len(found_path) - 1):
            plt.plot([pos[found_path[i]][0], pos[found_path[i + 1]][0]], [pos[found_path[i]][1], pos[found_path[i + 1]][1]], 'r-', linewidth=2)

    plt.show()

visualize_graph(graph, found_path)

