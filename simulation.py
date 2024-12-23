# Simulation of ACPC Grading System Server

import random
import math
from collections import deque

# Parameters
NUM_COMPUTERS = 10  # Number of available computers
SIMULATION_TIME = 18000  # 5 hours in seconds
MEAN_INTERARRIVAL = 35  # Average inter-arrival time (seconds)
MEAN_SERVICE_TIME = 42  # Average service time (seconds)

# Helper Functions
def exponential_random(mean):
    """
    Generate an exponentially distributed random number.
    :param mean: Mean value of the exponential distribution
    :return: Random number based on exponential distribution
    """
    return -mean * math.log(random.random())

# Initialization
computers = [0] * NUM_COMPUTERS  # Tracks the next free time for each computer
queue = deque()  # Queue for tasks waiting for service
clock = 0  # Simulation clock in seconds
total_delay_time = 0  # Accumulate delay time for tasks
total_waiting_time = 0  # Accumulate waiting time for tasks
tasks_processed = 0  # Number of tasks processed
queue_length_sum = 0  # Total queue length observed

# Simulation Loop
while clock < SIMULATION_TIME:
    # Generate inter-arrival time and service time for the next task
    interarrival_time = exponential_random(MEAN_INTERARRIVAL)
    service_time = exponential_random(MEAN_SERVICE_TIME)
    clock += interarrival_time  # Move simulation clock forward

    # Check if any computer is free
    free_computer = None
    for i in range(NUM_COMPUTERS):
        if computers[i] <= clock:
            free_computer = i
            break

    if free_computer is not None:
        # Assign task to the free computer
        computers[free_computer] = clock + service_time
        total_waiting_time += service_time
        tasks_processed += 1  # counting the number of tasks processed
    else:
        # Add task to the queue
        queue.append((clock, service_time))

    # Process tasks in the queue as computers become available
    while queue and any(c <= clock for c in computers):
        task_arrival, task_service_time = queue.popleft()
        free_computer = min(range(NUM_COMPUTERS), key=lambda x: computers[x])
        delay_time = max(0, computers[free_computer] - task_arrival)
        total_delay_time += delay_time
        total_waiting_time += task_service_time + delay_time
        computers[free_computer] += task_service_time
        tasks_processed += 1  # counting the number of tasks processed

    # Track queue length
    queue_length_sum += len(queue)

# Calculate Metrics
average_delay_time = total_delay_time / tasks_processed
average_waiting_time = total_waiting_time / tasks_processed
average_queue_length = queue_length_sum / (SIMULATION_TIME / MEAN_INTERARRIVAL)

# Output Results
print("Simulation Results:")
print(f"Average Delay Time: {average_delay_time:.2f} seconds")
print(f"Average Waiting Time: {average_waiting_time:.2f} seconds")
print(f"Average Queue Length: {average_queue_length:.2f} tasks")
