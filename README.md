<!-- # ACPC Grading System Server Simulation

## Project Overview
This project simulates the ACPC grading system server, which processes tasks (problems submitted for grading) arriving at random intervals. The system comprises 10 computers, each capable of serving tasks. If all computers are busy, tasks are added to a queue. The simulation calculates:

1. **Average delay time**: Time tasks spend waiting in the queue.
2. **Average waiting time**: Time tasks spend in the queue and being processed.
3. **Average queue length**: Average number of tasks waiting in the queue over time.

The simulation runs for 5 hours (18,000 seconds) with the following specifications:
- Average inter-arrival time: 35 seconds
- Average service time: 42 seconds

## Features
- Simulates task arrivals and service using exponential distributions.
- Manages task scheduling with a queue for pending tasks.
- Tracks key metrics for system performance.

## Prerequisites
Ensure you have the following installed:
- Python 3.6 or higher

## Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd acpc-grading-simulation
   ```

## Usage
1. Run the simulation script:
   ```bash
   python simulation.py
   ```
2. The output will display the following metrics:
   - Average Delay Time
   - Average Waiting Time
   - Average Queue Length

## How It Works
1. **Initialization:**
   - The system initializes 10 computers, a queue for tasks, and statistics for tracking performance.

2. **Random Time Generation:**
   - Inter-arrival and service times are generated using an exponential distribution.

3. **Task Processing:**
   - If a computer is free, the task is processed immediately.
   - If all computers are busy, the task waits in the queue until a computer becomes available.

4. **Metrics Calculation:**
   - The program calculates the average delay time, waiting time, and queue length based on all tasks processed during the 5-hour simulation.

## Example Output
```text
Average Delay Time: 12.45 seconds
Average Waiting Time: 54.32 seconds
Average Queue Length: 3.27 tasks
```

## Files
- `simulation.py`: Main simulation script.
- `README.md`: Project documentation.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork this repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a Pull Request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any inquiries or issues, feel free to contact:
- **Name**: Hassan Mikawi
- **Email**: [hassansherif122202@gmail.com](mailto:hassansherif122202@gmail.com)

## Acknowledgments
This project was developed as part of the Computing Algorithms course at the Arab Academy of Science and Technology and Maritime Transport.
 -->

# ACPC Grading System Server Simulation

## Project Overview
This project simulates the ACPC grading system server, which processes tasks (problems submitted for grading) arriving at random intervals. The system comprises 10 computers, each capable of serving tasks. If all computers are busy, tasks are added to a queue. The simulation calculates:
1. **Average delay time** (time spent waiting in the queue).
2. **Average waiting time** (time in the queue + time being served).
3. **Average queue length** (average number of tasks waiting).

---

### **Specifications**
1. **Task Arrival:**
    - Tasks arrive at random intervals following an exponential distribution.
    - The average inter-arrival time is 35 seconds.

2. **Task Service Time:**
    - Each task requires a random amount of time to complete, based on an exponential distribution with an average of 42 seconds.

3. **Computers:**
    - There are 10 computers available to process tasks.
    - If a computer is free, it will start serving the next task immediately.
    - If all computers are busy, tasks wait in a queue.

4. **Simulation Time:**
    - The simulation will run for **5 hours** (18,000 seconds).

---

### **Project Breakdown**

#### **Part I: Algorithm Design**
We'll design an algorithm for the simulation. Here's the detailed step-by-step approach:

1. **Initialization:**
    - Create a list to represent the 10 computers. Each computer tracks when it will next be free.
    - Create a queue to store tasks waiting for service.
    - Set up variables for tracking statistics: total delay time, total waiting time, and total queue length.

2. **Generate Random Times:**
    - Use the exponential distribution formula to generate:
      - Inter-arrival times (`T_interarrival`): Time between successive tasks arriving.
      - Service times (`T_service`): Time required for each task to be processed.

    Formula:
    T = -ln(random number) / λ

    Where:
    - random number is uniformly distributed between 0 and 1 (generated using rand() or similar).
    - λ is the rate parameter: λ = 1 / (mean time).

3. **Simulate Task Arrivals and Processing:**
    - Start the simulation clock at 0.
    - For each new task:
      - Check if any computer is free.
         - If free, assign the task to the computer.
         - If busy, add the task to the queue.
      - Update the clock to handle the next task arrival.

4. **Process Statistics:**
    - Track the time spent in the queue for each task.
    - Track the total waiting time (queue time + service time).
    - Track the length of the queue at different points in time.

5. **End of Simulation:**
    - After 5 hours (18,000 seconds), calculate:
      - Average delay time: (Total Delay Time) / (Total Number of Tasks).
      - Average waiting time: (Total Waiting Time) / (Total Number of Tasks).
      - Average queue length: (Sum of Queue Lengths) / (Observation Points).
<!-- 
---

#### **Part II: Implementation**
We'll implement the design in Python. Below is the code.

```python
import random
import math
from collections import deque

# Parameters
NUM_COMPUTERS = 10
SIMULATION_TIME = 18000  # 5 hours in seconds
MEAN_INTERARRIVAL = 35
MEAN_SERVICE_TIME = 42

# Helper Functions
def exponential_random(mean):
     """Generate exponentially distributed random number."""
     return -mean * math.log(random.random())

# Initialization
computers = [0] * NUM_COMPUTERS  # Tracks when each computer will be free
queue = deque()  # Queue for waiting tasks
clock = 0    # Simulation clock
total_delay_time = 0
total_waiting_time = 0
queue_length_sum = 0
tasks_processed = 0

# Simulation
while clock < SIMULATION_TIME:
     # Generate the next task's interarrival time and service time
     interarrival_time = exponential_random(MEAN_INTERARRIVAL)
     service_time = exponential_random(MEAN_SERVICE_TIME)
     clock += interarrival_time  # Move the clock forward

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
     else:
          # Add task to the queue
          queue.append((clock, service_time))

     # Process tasks from the queue if computers free up
     while queue and any(c <= clock for c in computers):
          task_arrival, task_service_time = queue.popleft()
          free_computer = min(range(NUM_COMPUTERS), key=lambda x: computers[x])
          delay_time = computers[free_computer] - task_arrival
          total_delay_time += max(0, delay_time)
          total_waiting_time += task_service_time + max(0, delay_time)
          computers[free_computer] += task_service_time
          tasks_processed += 1

     # Update statistics
     queue_length_sum += len(queue)

# Results
average_delay_time = total_delay_time / tasks_processed
average_waiting_time = total_waiting_time / tasks_processed
average_queue_length = queue_length_sum / (SIMULATION_TIME / MEAN_INTERARRIVAL)

# Output
print(f"Average Delay Time: {average_delay_time:.2f} seconds")
print(f"Average Waiting Time: {average_waiting_time:.2f} seconds")
print(f"Average Queue Length: {average_queue_length:.2f} tasks")
```

--- -->

### **Testing**
1. Run the simulation multiple times to verify the output.
2. Cross-check that the results align with theoretical expectations (based on exponential distribution properties).
