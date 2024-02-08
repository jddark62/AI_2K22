import random

# Define the goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Define the initial population
def generate_initial_population(population_size):
    population = []
    for _ in range(population_size):
        state = random.sample(range(9), 9)
        state = [state[i:i+3] for i in range(0, 9, 3)]
        population.append(state)
    return population

# Calculate the fitness of an individual
def calculate_fitness(state):
    fitness = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                fitness += 1
    return fitness

# Select parents for crossover using tournament selection
def tournament_selection(population, k):
    selected_parents = []
    for _ in range(2):
        tournament = random.sample(population, k)
        selected_parents.append(min(tournament, key=calculate_fitness))
    return selected_parents

# Perform crossover to create new offspring
def crossover(parent1, parent2):
    offspring = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            if random.random() < 0.5:
                offspring[i][j] = parent1[i][j]
            else:
                offspring[i][j] = parent2[i][j]
    return offspring

# Perform mutation on an individual
def mutate(state):
    i, j = random.randint(0, 2), random.randint(0, 2)
    new_state = [row[:] for row in state]
    new_state[i][j] = random.choice([x for x in range(9) if x != state[i][j]])
    return new_state

# Solve the 8-puzzle problem using genetic algorithm
def solve_8_puzzle(population_size, tournament_size, mutation_rate, max_generations):
    population = generate_initial_population(population_size)
    for generation in range(max_generations):
        population = sorted(population, key=calculate_fitness)
        if calculate_fitness(population[0]) == 0:
            return population[0]
        new_population = [population[0]]
        while len(new_population) < population_size:
            parent1, parent2 = tournament_selection(population, tournament_size)
            offspring = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                offspring = mutate(offspring)
            new_population.append(offspring)
        population = new_population
    return None

# Example usage
solution = solve_8_puzzle(population_size=100, tournament_size=10, mutation_rate=0.1, max_generations=1000)
if solution:
    print("Solution found:")
    for row in solution:
        print(row)
else:
    print("No solution found within the given number of generations.")
