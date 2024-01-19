from collections import deque

def solve_water_jug_problem(capacity_jug1, capacity_jug2, target):
    # Create a queue for BFS
    queue = deque()
    
    # Create a set to keep track of visited states
    visited = set()
    
    # Initialize the initial state with both jugs empty
    initial_state = (0, 0)
    
    # Add the initial state to the queue
    queue.append(initial_state)
    
    # BFS loop
    while queue:
        # Get the current state from the queue
        current_state = queue.popleft()
        
        # Check if the current state is the target state
        if current_state[0] == target or current_state[1] == target:
            return True
        
        # Generate all possible next states
        next_states = []
        
        # Fill jug 1
        next_states.append((capacity_jug1, current_state[1]))
        
        # Fill jug 2
        next_states.append((current_state[0], capacity_jug2))
        
        # Empty jug 1
        next_states.append((0, current_state[1]))
        
        # Empty jug 2
        next_states.append((current_state[0], 0))
        
        # Pour from jug 1 to jug 2
        pour_amount = min(current_state[0], capacity_jug2 - current_state[1])
        next_states.append((current_state[0] - pour_amount, current_state[1] + pour_amount))
        
        # Pour from jug 2 to jug 1
        pour_amount = min(current_state[1], capacity_jug1 - current_state[0])
        next_states.append((current_state[0] + pour_amount, current_state[1] - pour_amount))
        
        # Add the next states to the queue if they haven't been visited before
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
    
    # If the target state is not reachable, return False
    return False

# Example usage
capacity_jug1 = 5
capacity_jug2 = 3
target = 4

result = solve_water_jug_problem(capacity_jug1, capacity_jug2, target)
print(result)

