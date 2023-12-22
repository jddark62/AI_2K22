import networkx as nx
import matplotlib.pyplot as plt

# Perform BFS to find the optimal path
def bfs(graph, start, end):
    visited = set()
    queue = [[start]]
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node == end:
            return path
        
        if node not in visited:
            neighbors = graph[node]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
            visited.add(node)
    
    return None

# Perform DFS to find the optimal path
def dfs(graph, start, end):
    visited = set()
    stack = [[start]]
    
    while stack:
        path = stack.pop()
        node = path[-1]
        
        if node == end:
            return path
        
        if node not in visited:
            neighbors = graph[node]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
                
            visited.add(node)
    
    return None

# Construct and visualize multiple graphs
graphs = [
    {
        'nodes': [1, 2, 3, 4, 5, 6],
        'edges': [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)],
        'source': 1,
        'destination': 6
    },
    {
        'nodes': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'edges': [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 9), (6, 10)],
        'source': 1,
        'destination': 10
    }
]

for graph_data in graphs:
    # Create a graph
    G = nx.Graph()
    G.add_nodes_from(graph_data['nodes'])
    G.add_edges_from(graph_data['edges'])

    # Define source and destination nodes
    source = graph_data['source']
    destination = graph_data['destination']

    # Find the optimal path using BFS
    optimal_path_bfs = bfs(G, source, destination)

    # Find the optimal path using DFS
    optimal_path_dfs = dfs(G, source, destination)

    if optimal_path_bfs:
        print("Optimal path (BFS):", optimal_path_bfs)
        
        # Highlight the optimal path (BFS)
        edge_colors_bfs = ['blue' if (u, v) in zip(optimal_path_bfs, optimal_path_bfs[1:]) else 'gray' for u, v in G.edges()]
        node_colors_bfs = ['blue' if node in optimal_path_bfs else 'gray' for node in G.nodes()]

        # Visualize the graph (BFS)
        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos, node_color=node_colors_bfs, edge_color=edge_colors_bfs, with_labels=True)
        plt.show()
    else:
        print("No path exists between the source and destination (BFS).")

    if optimal_path_dfs:
        print("Optimal path (DFS):", optimal_path_dfs)
        
        # Highlight the optimal path (DFS)
        edge_colors_dfs = ['blue' if (u, v) in zip(optimal_path_dfs, optimal_path_dfs[1:]) else 'gray' for u, v in G.edges()]
        node_colors_dfs = ['blue' if node in optimal_path_dfs else 'gray' for node in G.nodes()]

        # Visualize the graph (DFS)
        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos, node_color=node_colors_dfs, edge_color=edge_colors_dfs, with_labels=True)
        plt.show()
    else:
        print("No path exists between the source and destination (DFS).")
