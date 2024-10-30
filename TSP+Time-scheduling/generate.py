import random
import math
from datetime import datetime, timedelta
def read_input(filename):
    """Reads customer locations and IDs from a file."""
    locations = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.split()
            customer_id = int(data[0])
            x = float(data[1])
            y = float(data[2])
            locations.append((customer_id, x, y))
    return locations

def generate_random_time_windows(num_customers):
    """Generate random delivery time windows for customers."""
    time_windows = []
    for _ in range(num_customers):
        start_hour = random.randint(8, 14)  # Start between 8 AM and 2 PM
        end_hour = start_hour + random.randint(1, 3)  # End 1-3 hours later
        time_windows.append((start_hour, end_hour))
    return time_windows


def write_test_file(locations, time_windows, filename='test_customers.txt'):
    """Write customer locations and time windows to a text file."""
    with open(filename, 'w') as file:
        for (i, (x, y)), (start, end) in zip(locations, time_windows):
            file.write(f"{i} {x} {y} {start} {end}\n")
    print(f"Test file '{filename}' generated successfully.")
if __name__ == "__main__":
    # List of customer locations (from your input)
    locations = [
        (1, 565.0, 575.0), (2, 25.0, 185.0), (3, 345.0, 750.0), 
        (4, 945.0, 685.0), (5, 845.0, 655.0), (6, 880.0, 660.0),
        (7, 25.0, 230.0), (8, 525.0, 1000.0), (9, 580.0, 1175.0),
        (10, 650.0, 1130.0), (11, 1605.0, 620.0), (12, 1220.0, 580.0),
        (13, 1465.0, 200.0), (14, 1530.0, 5.0), (15, 845.0, 680.0),
        (16, 725.0, 370.0), (17, 145.0, 665.0), (18, 415.0, 635.0),
        (19, 510.0, 875.0), (20, 560.0, 365.0), (21, 300.0, 465.0),
        (22, 520.0, 585.0), (23, 480.0, 415.0), (24, 835.0, 625.0),
        (25, 975.0, 580.0), (26, 1215.0, 245.0), (27, 1320.0, 315.0),
        (28, 1250.0, 400.0), (29, 660.0, 180.0), (30, 410.0, 250.0),
        (31, 420.0, 555.0), (32, 575.0, 665.0), (33, 1150.0, 1160.0),
        (34, 700.0, 580.0), (35, 685.0, 595.0), (36, 685.0, 610.0),
        (37, 770.0, 610.0), (38, 795.0, 645.0), (39, 720.0, 635.0),
        (40, 760.0, 650.0), (41, 475.0, 960.0), (42, 95.0, 260.0),
        (43, 875.0, 920.0), (44, 700.0, 500.0), (45, 555.0, 815.0),
        (46, 830.0, 485.0), (47, 1170.0, 65.0), (48, 830.0, 610.0),
        (49, 605.0, 625.0), (50, 595.0, 360.0), (51, 1340.0, 725.0),
        (52, 1740.0, 245.0)
    ]

    # Generate random time windows for each customer
    time_windows = generate_random_time_windows(len(locations))

    # Write the data to a file for testing
    write_test_file(locations, time_windows)
