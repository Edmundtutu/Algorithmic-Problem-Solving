import math
from datetime import datetime, timedelta
import time  # To measure execution time

# Step 1: Read the data from the file (locations + time windows)
def read_test_data(filename):
    """Read warehouse and customer data (locations + time windows) from a file."""
    locations = []
    time_windows = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing spaces and newlines
            if not line:  # Skip empty lines
                continue

            data = line.split()
            if len(data) < 5:  # Ensure the line has the required number of elements
                print(f"Skipping invalid line: {line}")
                continue

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

# Step 4: Depth-First Search (DFS) Implementation
def dfs(locations, time_windows):
    """Depth-First Search to find the optimal delivery route."""
    num_locations = len(locations)
    best_route = None
    best_score = float('inf')

    def dfs_helper(route, current_cost):
        nonlocal best_route, best_score

        # If we visited all locations and returned to the warehouse
        if len(route) == num_locations + 1 and route[-1] == 0:
            score = fitness(route, locations, time_windows)
            if score < best_score:
                best_score = score
                best_route = route
            return

        # Explore further by visiting unvisited locations
        for i in range(1, num_locations):
            if i not in route:
                new_route = route + [i]
                new_cost = current_cost + distance(locations[route[-1]], locations[i])
                dfs_helper(new_route, new_cost)

    # Start DFS from the warehouse (0)
    dfs_helper([0], 0)
    return best_route, best_score

# Step 5: Run the DFS with Execution Time Measurement
if __name__ == "__main__":
    filename = "test_customers.txt"
    locations, time_windows = read_test_data(filename)

    # Measure the execution time
    start_time = time.time()
    best_route, best_score = dfs(locations, time_windows)
    end_time = time.time()
    elapsed_time = end_time - start_time

    print("Best Route (DFS):", best_route)
    print("Best Score (DFS):", best_score)
    print(f"Elapsed Time (DFS): {elapsed_time:.2f} seconds")
