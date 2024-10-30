import random
import math
from datetime import datetime, timedelta
import time  # Import the time module to measure execution time

# Step 1: Read the data from the file (locations + time windows)
def read_test_data(filename):
    """Read warehouse and customer data (locations + time windows) from a file."""
    locations = []
    time_windows = []

    with open(filename, 'r') as file:
        for line in file:
            data = line.split()
            customer_id = int(data[0])
            x, y = float(data[1]), float(data[2])
            start_hour, end_hour = int(data[3]), int(data[4])
            locations.append((customer_id, x, y))
            time_windows.append((start_hour, end_hour))

    return locations, time_windows

# Step 2: Calculate the Euclidean distance between two locations
def distance(loc1, loc2):
    """Calculate Euclidean distance between two points."""
    x1, y1 = loc1[1], loc1[2]
    x2, y2 = loc2[1], loc2[2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Step 3: Fitness function (total distance + penalty for missed time windows)
def fitness(route, locations, time_windows):
    total_distance = 0
    penalty = 0
    current_time = datetime(2024, 10, 28, 8, 0)  # Start time at 8 AM

    for i in range(len(route) - 1):
        loc1, loc2 = locations[route[i]], locations[route[i + 1]]
        total_distance += distance(loc1, loc2)

        travel_time = timedelta(minutes=distance(loc1, loc2) * 2)  # Assume 1 km = 2 min
        current_time += travel_time

        customer_id = route[i + 1]
        start_hour, end_hour = time_windows[customer_id]
        if not (start_hour <= current_time.hour <= end_hour):
            penalty += 1000  # Penalty for violating the time window

    return total_distance + penalty

# Step 4: Initialize the population with random routes
def initialize_population(num_customers, population_size=50):
    population = []
    for _ in range(population_size):
        route = list(range(1, num_customers))  # Exclude warehouse (0)
        random.shuffle(route)
        route = [0] + route + [0]  # Start and end at the warehouse
        population.append(route)
    return population

# Step 5: Select parents using tournament selection
def select_parents(population, scores):
    candidates = random.sample(list(zip(population, scores)), 5)
    parents = sorted(candidates, key=lambda x: x[1])[:2]
    return parents[0][0], parents[1][0]

# Step 6: Perform order-based crossover with retry mechanism
def crossover_with_retry(parent1, parent2, max_attempts=10):
    """Try generating valid children within a limited number of attempts."""
    for _ in range(max_attempts):
        child1, child2 = crossover(parent1, parent2)
        if None not in child1 and None not in child2:
            return child1, child2
    print("Warning: Failed to produce valid children after retries.")
    return parent1, parent2  # Fallback to parents if children are invalid

def crossover(parent1, parent2):
    size = len(parent1) - 2  # Exclude warehouse
    start, end = sorted(random.sample(range(1, size + 1), 2))

    child1 = [None] * len(parent1)
    child2 = [None] * len(parent2)

    child1[1:start] = parent1[1:start]
    child2[1:start] = parent2[1:start]

    fill_remaining_cities(child1, parent2, start, end)
    fill_remaining_cities(child2, parent1, start, end)

    child1[0] = child1[-1] = 0
    child2[0] = child2[-1] = 0

    return child1, child2

def fill_remaining_cities(child, parent, start, end):
    idx = end
    for city in parent:
        if city not in child:
            if idx == len(child) - 1:
                idx = 1  # Wrap around
            child[idx] = city
            idx += 1

# Step 7: Apply mutation by swapping two cities
def mutation(route, mutation_rate=0.1):
    if random.random() < mutation_rate:
        i, j = random.sample(range(1, len(route) - 1), 2)
        route[i], route[j] = route[j], route[i]
    return route

# Step 8: Main GA loop with timing
def genetic_algorithm(locations, time_windows, num_generations=100, population_size=50):
    population = initialize_population(len(locations), population_size)
    best_route = None
    best_score = float('inf')

    # Start the timer
    start_time = time.time()

    for _ in range(num_generations):
        scores = [fitness(route, locations, time_windows) for route in population]
        for route, score in zip(population, scores):
            if score < best_score:
                best_score = score
                best_route = route

        parent1, parent2 = select_parents(population, scores)
        child1, child2 = crossover_with_retry(parent1, parent2)

        child1 = mutation(child1)
        child2 = mutation(child2)

        population[-2:] = [child1, child2]

    # End the timer
    end_time = time.time()
    elapsed_time = end_time - start_time

    return best_route, best_score, elapsed_time

# Step 9: Run the GA with the test file
if __name__ == "__main__":
    filename = "smaller.txt"
    locations, time_windows = read_test_data(filename)

    best_route, best_score, elapsed_time = genetic_algorithm(locations, time_windows)
    print("Best Route:", best_route)
    print("Best Score:", best_score)
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")
