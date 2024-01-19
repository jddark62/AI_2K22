import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_binary_tree():
    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')
    root.right.left = Node('F')
    root.right.right = Node('G')
    return root

def heuristic(node, goal):
    # Assigning random heuristic values
    heuristic_values = {'A': 3, 'B': 2, 'C': 4, 'D': 1, 'E': 5, 'F': 2, 'G': 3}
    return heuristic_values[node]

def a_star_search(root, start, goal, heuristic):
    open_set = [(0, start)]
    came_from = {}
    g_score = {node.value: float('inf') for node in flatten_tree(root)}
    g_score[start] = 0
    f_score = {node.value: float('inf') for node in flatten_tree(root)}
    f_score[start] = heuristic(start, goal)

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            return reconstruct_path(came_from, goal)

        for child in get_children(root, current):
            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score[child.value]:
                came_from[child.value] = current
                g_score[child.value] = tentative_g_score
                f_score[child.value] = tentative_g_score + heuristic(child.value, goal)
                heapq.heappush(open_set, (f_score[child.value], child.value))

    return None

def flatten_tree(root):
    if root is None:
        return []
    return [root] + flatten_tree(root.left) + flatten_tree(root.right)

def get_children(root, value):
    node = find_node(root, value)
    if node is None:
        return []
    children = []
    if node.left:
        children.append(node.left)
    if node.right:
        children.append(node.right)
    return children

def find_node(root, value):
    if root is None or root.value == value:
        return root
    left_result = find_node(root.left, value)
    if left_result:
        return left_result
    return find_node(root.right, value)

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

def visualize_tree(root, path):
    graph = nx.Graph()
    add_nodes(graph, root)
    add_edges(graph, root)
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_edges(graph, pos)
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edges(graph, pos, edgelist=[(path[i], path[i+1]) for i in range(len(path)-1)], edge_color='r', width=2)
    plt.show()

def add_nodes(graph, root):
    if root is None:
        return
    graph.add_node(root.value)
    add_nodes(graph, root.left)
    add_nodes(graph, root.right)

def add_edges(graph, root):
    if root is None:
        return
    if root.left:
        graph.add_edge(root.value, root.left.value)
    if root.right:
        graph.add_edge(root.value, root.right.value)
    add_edges(graph, root.left)
    add_edges(graph, root.right)

root = construct_binary_tree()
start = 'A'
goal = 'G'

path = a_star_search(root, start, goal, heuristic)
if path:
    visualize_tree(root, path)
else:
    print("No path found.")
