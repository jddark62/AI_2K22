from collections import deque

# Define the goal state
goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Define the initial state
initial_state = [7, 2, 4, 5, 0, 6, 8, 3, 1]

# Define the possible moves
moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

# Function to swap two elements in a list
def swap(state, i, j):
    state[i], state[j] = state[j], state[i]
    return state

# Function to check if two states are equal
def is_equal(state1, state2):
    return state1 == state2

# Function to generate the next possible states
def generate_next_states(state):
    next_states = []
    zero_index = state.index(0)
    for move in moves[zero_index]:
        next_state = swap(state.copy(), zero_index, move)
        next_states.append(next_state)
    return next_states

# Function to perform breadth-first search
def bfs(initial_state, goal_state):
    visited = set()
    queue = deque([(initial_state, [])])
    while queue:
        state, path = queue.popleft()
        if is_equal(state, goal_state):
            return path
        if tuple(state) not in visited:
            visited.add(tuple(state))
            next_states = generate_next_states(state)
            for next_state in next_states:
                queue.append((next_state, path + [next_state]))

    return None

# Solve the 8 puzzle problem using BFS
solution = bfs(initial_state, goal_state)

# Visualize the initial state
print("Initial state:")
print(f"{initial_state[0]} {initial_state[1]} {initial_state[2]}")
print(f"{initial_state[3]} {initial_state[4]} {initial_state[5]}")
print(f"{initial_state[6]} {initial_state[7]} {initial_state[8]}")
print()

# Visualize the solution
if solution:
    print("Solution found!")
    for i, state in enumerate(solution):
        print(f"Step {i+1}:")
        print(f"{state[0]} {state[1]} {state[2]}")
        print(f"{state[3]} {state[4]} {state[5]}")
        print(f"{state[6]} {state[7]} {state[8]}")
        print()
else:
    print("No solution found.")
