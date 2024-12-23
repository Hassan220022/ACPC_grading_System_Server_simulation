import random
import math
from collections import deque

# ------------------------------
#  Simulation Parameters
# ------------------------------
# NUM_COMPUTERS = 10       # Fewer computers => higher chance of forming a queue
# SIMULATION_TIME = 18000  # 5 hours in seconds
# MEAN_INTERARRIVAL = 9   # Smaller => higher arrival rate (~0.111 tasks/sec)
# MEAN_SERVICE_TIME = 40  # Each computer's service rate is ~0.025 tasks/sec

# 
NUM_COMPUTERS = 10       # Fewer computers => higher chance of forming a queue
SIMULATION_TIME = 18000  # 5 hours in seconds
MEAN_INTERARRIVAL = 35   # Smaller => higher arrival rate (~0.111 tasks/sec)
MEAN_SERVICE_TIME = 42  # Each computer's service rate is ~0.025 tasks/sec

def exponential_random(mean):
    """
    Generate an exponentially distributed random number using the inverse transform method:
    X = -mean * ln(U),  where U ~ Uniform(0,1).
    """
    return -mean * math.log(random.random())

# ------------------------------
#  Initialization
# ------------------------------
computers = [0.0] * NUM_COMPUTERS  # Tracks "next free time" for each computer
queue = deque()                    # FIFO queue for waiting tasks

clock = 0.0                        # Simulation clock in seconds
tasks_processed = 0

# Accumulators for performance metrics
total_delay_time = 0.0   # Sum of queueing delays (arrival -> start of service)
total_waiting_time = 0.0 # Sum of total time in system (delay + service)
queue_area = 0.0         # For time-based average queue length

last_event_time = 0.0    # Time of the last arrival/queue-processing event

# ------------------------------
#  Simulation Loop
# ------------------------------
while clock < SIMULATION_TIME:
    # 1) Accumulate area under the queue-length curve since last event
    dt = clock - last_event_time
    queue_area += len(queue) * dt
    last_event_time = clock
    
    # 2) Generate the next arrival
    interarrival_time = exponential_random(MEAN_INTERARRIVAL)
    service_time = exponential_random(MEAN_SERVICE_TIME)
    
    clock += interarrival_time
    if clock > SIMULATION_TIME:
        break  # Stop arrivals if we've exceeded the simulation window
    
    # 3) Check if any computer is free at this new arrival time
    free_computer = None
    for i in range(NUM_COMPUTERS):
        if computers[i] <= clock:
            free_computer = i
            break
    
    if free_computer is not None:
        # Computer is free => start service immediately
        computers[free_computer] = clock + service_time
        # No queueing delay
        delay_time = 0.0
        total_delay_time += delay_time
        # Waiting time (system time) is just service time
        total_waiting_time += (delay_time + service_time)
        tasks_processed += 1
    else:
        # No computer free => put the task in queue
        queue.append((clock, service_time))
    
    # 4) After the arrival, see if we can process tasks in the queue
    while queue and any(comp <= clock for comp in computers):
        # Integrate queue length up to this moment
        dt = clock - last_event_time
        queue_area += len(queue) * dt
        last_event_time = clock
        
        arrival_time_q, service_time_q = queue.popleft()
        # Find the soonest available computer
        free_computer = min(range(NUM_COMPUTERS), key=lambda x: computers[x])
        
        # The task can start service no earlier than the computer is free
        start_of_service = max(clock, computers[free_computer])
        delay_time = start_of_service - arrival_time_q  # queue wait
        total_delay_time += delay_time
        
        # waiting time = delay + service
        total_waiting_time += (delay_time + service_time_q)
        
        computers[free_computer] = start_of_service + service_time_q
        tasks_processed += 1

# --- One last integration after we stop arrivals ---
if clock < SIMULATION_TIME:
    dt = SIMULATION_TIME - last_event_time
    queue_area += len(queue) * dt
else:
    dt = clock - last_event_time
    queue_area += len(queue) * dt

# ------------------------------
#  Calculate Final Metrics
# ------------------------------
if tasks_processed > 0:
    average_delay_time = total_delay_time / tasks_processed
    average_waiting_time = total_waiting_time / tasks_processed
else:
    average_delay_time = 0.0
    average_waiting_time = 0.0

# Time-based average queue length
average_queue_length = queue_area / SIMULATION_TIME

# ------------------------------
#  Output Results
# ------------------------------
print("Simulation Results:")
print(f"Tasks Processed:       {tasks_processed}")
print(f"Average Delay Time:    {average_delay_time:.2f} seconds  (queue wait)")
print(f"Average Waiting Time:  {average_waiting_time:.2f} seconds (delay + service)")
print(f"Average Queue Length:  {average_queue_length:.2f} tasks   (time-based)")
