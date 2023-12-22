import networkx as nx
import matplotlib.pyplot as plt

def iterative_deepening_search(graph, source, destination, depth_limit):
    for depth in range(depth_limit):
        visited = set()
        path = []
        if dfs(graph, source, destination, depth, visited, path):
            return path
    return None

def dfs(graph, current, destination, depth, visited, path):
    if current == destination:
        path.append(current)
        return True
    if depth <= 0:
        return False
    visited.add(current)
    for neighbor in graph[current]:
        if neighbor not in visited:
            if dfs(graph, neighbor, destination, depth - 1, visited, path):
                path.append(current)
                return True
    return False

# Create a sample graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Set the source and destination nodes
source = 'A'
destination = 'F'

# Set the depth limit
depth_limit = 4

# Perform iterative deepening search
path = iterative_deepening_search(graph, source, destination, depth_limit)

# Visualize the graph
G = nx.Graph(graph)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='lightblue')
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
if path:
    path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
plt.axis('off')
plt.show()
