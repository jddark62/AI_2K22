import random

class WaterJugProblem:
    def __init__(self, jug1_capacity, jug2_capacity, target_amount):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target_amount = target_amount

    def generate_initial_state(self):
        return (0, 0)  # Initial state with both jugs empty

    def generate_random_action(self):
        action = random.choice(["fill_jug1", "fill_jug2", "empty_jug1", "empty_jug2", "pour_jug1_to_jug2", "pour_jug2_to_jug1"])
        return action

    def apply_action(self, state, action):
        jug1_amount, jug2_amount = state

        if action == "fill_jug1":
            jug1_amount = self.jug1_capacity
        elif action == "fill_jug2":
            jug2_amount = self.jug2_capacity
        elif action == "empty_jug1":
            jug1_amount = 0
        elif action == "empty_jug2":
            jug2_amount = 0
        elif action == "pour_jug1_to_jug2":
            amount_to_pour = min(jug1_amount, self.jug2_capacity - jug2_amount)
            jug1_amount -= amount_to_pour
            jug2_amount += amount_to_pour
        elif action == "pour_jug2_to_jug1":
            amount_to_pour = min(jug2_amount, self.jug1_capacity - jug1_amount)
            jug2_amount -= amount_to_pour
            jug1_amount += amount_to_pour

        return (jug1_amount, jug2_amount)

    def evaluate_fitness(self, state):
        jug1_amount, jug2_amount = state
        difference = abs(jug1_amount + jug2_amount - self.target_amount)
        fitness = 1 / (difference + 1)  # Higher fitness for states closer to the target amount
        return fitness

    def solve(self, population_size, max_generations):
        population = [self.generate_initial_state() for _ in range(population_size)]

        for generation in range(max_generations):
            fitness_scores = [self.evaluate_fitness(state) for state in population]
            best_state = population[fitness_scores.index(max(fitness_scores))]

            if max(fitness_scores) == 1:
                return best_state

            new_population = [best_state]

            while len(new_population) < population_size:
                parent1 = self.select_parent(population, fitness_scores)
                parent2 = self.select_parent(population, fitness_scores)
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                new_population.append(child)

            population = new_population

        return None

    def select_parent(self, population, fitness_scores):
        total_fitness = sum(fitness_scores)
        probabilities = [fitness / total_fitness for fitness in fitness_scores]
        return random.choices(population, probabilities)[0]

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, len(parent1) - 1)
        child = parent1[:crossover_point] + parent2[crossover_point:]
        return child

    def mutate(self, state):
        action = self.generate_random_action()
        return self.apply_action(state, action)

# Example usage
jug1_capacity = 5
jug2_capacity = 3
target_amount = 4

problem = WaterJugProblem(jug1_capacity, jug2_capacity, target_amount)
solution = problem.solve(population_size=100, max_generations=1000)
print("Solution:", solution)
