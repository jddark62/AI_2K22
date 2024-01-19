import random
import matplotlib.pyplot as plt

def hill_climbing_search(problem, max_iterations):
    current_state = problem.initial_state()
    best_state = current_state
    best_score = problem.evaluate(current_state)
    scores = [best_score]

    for _ in range(max_iterations):
        neighbors = problem.generate_neighbors(current_state)
        random.shuffle(neighbors)

        found_better_neighbor = False
        for neighbor in neighbors:
            neighbor_score = problem.evaluate(neighbor)
            if neighbor_score > best_score:
                current_state = neighbor
                best_score = neighbor_score
                found_better_neighbor = True
                break

        if not found_better_neighbor:
            break

        scores.append(best_score)

    return best_state, scores

# Example usage
class Problem:
    def initial_state(self):
        return random.randint(0, 100)

    def evaluate(self, state):
        return -abs(state - 50)  # Minimize the distance from 50

    def generate_neighbors(self, state):
        return [state + random.randint(-10, 10) for _ in range(10)]

problem = Problem()
best_state, scores = hill_climbing_search(problem, max_iterations=100)

# Visualize the scores
plt.plot(scores)
plt.xlabel('Iteration')
plt.ylabel('Score')
plt.title('Hill Climbing Search')
plt.show()
