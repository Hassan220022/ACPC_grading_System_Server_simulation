# ACPC Grading System Server Simulation

This project simulates an **ACPC Grading System Server** where multiple computers process incoming tasks (contest problem submissions). Tasks arrive at random intervals, each requiring a random (exponential) amount of service time. If no computer is available, the tasks wait in a queue until a computer becomes free.

## Table of Contents

- [Features](#features)  
- [Requirements and Dependencies](#requirements-and-dependencies)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Simulation Details](#simulation-details)  
- [Key Formulas](#key-formulas)  
- [Project Structure](#project-structure)  
- [Output and Metrics](#output-and-metrics)  
- [Parameter Tuning](#parameter-tuning)  
- [Interpreting Results](#interpreting-results)  
- [Possible Extensions](#possible-extensions)  
- [Troubleshooting](#troubleshooting)  
- [References](#references)  
- [License](#license)

---

## Features

1. **Multiple Servers (Computers):**  
   - The code simulates up to 10 computers (by default), each of which can handle one task at a time.

2. **Exponential Interarrival and Service Times:**  
   - Arrival times and service times are drawn from exponential distributions with configurable mean parameters.

3. **FIFO Queue Mechanism:**  
   - Tasks that arrive when no computer is free wait in a queue (First-In, First-Out).

4. **Performance Metrics:**  
   - Reports **average delay time** (time spent waiting in queue before service).  
   - Reports **average waiting time** (time in queue + service time).  
   - Reports **time-based average queue length**.

5. **Event-Driven Elements:**  
   - The simulator updates the clock by interarrival events and processes queued tasks whenever servers become free.

---

## Requirements and Dependencies

- **Python 3.7+** (Tested on Python 3.7, 3.8, 3.9)  
- Standard libraries:
  - `random`  
  - `math`  
  - `collections.deque`

No additional third-party libraries are required.

---

## Installation

1. **Clone or download** this repository to your local machine.  
2. Ensure you have Python 3.7 or later installed.
3. From your terminal, navigate to the project folder:
   ```bash
   cd path/to/acpc_grading_system_server_simulation
   ```
4. There is no special installation step; everything runs as is.

---

## Usage

Run the simulation script directly via Python:

```bash
python3 simulation.py
```

Where `simulation.py` is the name of the Python file containing the simulation code.

### Configuring Simulation Parameters

Inside the script, you will see constants such as:

```python
NUM_COMPUTERS = 10      # Number of available computers
SIMULATION_TIME = 18000 # 5 hours in seconds
MEAN_INTERARRIVAL = 35  # Average interarrival time (seconds)
MEAN_SERVICE_TIME = 42  # Average service time (seconds)
```

You can edit these parameters to run experiments with different settings.

---

## Simulation Details

1. **Interarrival Times**  
   - Generated using an exponential distribution with mean `MEAN_INTERARRIVAL`.
   - If `U ~ Uniform(0,1)`, then  
     `T_arrival = - (MEAN_INTERARRIVAL) * ln(U)`.

2. **Service Times**  
   - Also exponentially distributed with mean `MEAN_SERVICE_TIME`.
   - If `U' ~ Uniform(0,1)`, then  
     `T_service = - (MEAN_SERVICE_TIME) * ln(U')`.

3. **Queueing Mechanism**  
   - Each time an arrival occurs, if a computer is free at that time, the task starts service immediately. Otherwise, it joins a FIFO queue.  
   - When a computer completes a task or is found idle, any queued tasks are served in arrival order.

4. **Time-Based Queue Length**  
   - The code continuously accumulates an "area under the queue length curve" over time. Dividing that area by the total simulation time yields the time-averaged queue length. Formally, if `Q(t)` is the queue length at time `t`, then  
     `L_q = (1 / T) * integral from 0 to T of Q(t) dt`,  
     where `T` is the total simulation time (e.g., 5 hours).


---

## Key Formulas

The simulator uses several **key formulas** based on **queueing theory** and **exponential distributions**:

1. **Exponential Distribution**  
   - To generate an exponentially distributed random variable X with mean α:
     - X = -α * ln(U), where U is a random variable uniformly distributed between 0 and 1.
   - In this project:
     - α = MEAN_INTERARRIVAL for interarrival times.  
     - α = MEAN_SERVICE_TIME for service times.

2. **Arrival Rate and Service Rate**  
   - **Arrival rate**: λ = 1 / MEAN_INTERARRIVAL.  
   - **Service rate** (per computer): μ = 1 / MEAN_SERVICE_TIME.  

3. **Delay Time (D)**  
   - For each task, **delay** = time spent waiting in the queue before service begins.  
   - In code, if a task arrives at time a and begins service at time s, then  
     - D = s - a.

4. **Waiting Time (W)**  
   - **Waiting time** = total time in system = **delay** + **service time**.  
   - For a task that arrives at time a, begins service at s, and completes at c,  
     - W = (s - a) + (c - s) = c - a.

5. **Averaging Metrics**  
   - After simulating all tasks (up to the 5-hour window), we compute:  
     - Average Delay = (sum of all D_i) / (Number of tasks),
     - Average Waiting Time = (sum of all W_i) / (Number of tasks).
   - For **time-based** average queue length:
     - Average Queue Length = (1 / T) * integral from 0 to T of Q(t) dt,
     which the code approximates by summing up (queue length * Δt) over each event interval.

---

## Project Structure

```
acpc_grading_system_server_simulation/
├── README.md                      # This README file
├── simulation.py   # Main Python script
└── ...
```

- **`simulation.py`**  
  This file contains the entire simulation logic. Key sections include:
  - **Initialization** of variables (e.g., `computers`, `queue`, accumulators).  
  - **Main Loop** where arrivals are generated and tasks are processed.  
  - **Statistics Computation** at the end (average delays, queue length, etc.).  
  - **Result Output** printed to the console.

---

## Output and Metrics

Upon completion, the script prints metrics like:

```
Simulation Results:
Tasks Processed: 1286
Average Delay Time: 10.65 seconds  (queue wait only)
Average Waiting Time: 52.33 seconds (delay + service)
Average Queue Length: 3.12 tasks   (time-based)
```

- **Tasks Processed**: The total number of tasks that arrived and were served within the simulation window.  
- **Average Delay Time**: The mean time tasks spent waiting in the queue before service.  
- **Average Waiting Time**: The mean total time in system (queue wait + service).  
- **Time-Based Average Queue Length**: The mean number of tasks in the queue at any moment, over the entire simulation duration.

---

## Parameter Tuning

By default, the simulation is configured with:

```python
NUM_COMPUTERS = 10
SIMULATION_TIME = 18000  # 5 hours
MEAN_INTERARRIVAL = 35   # seconds
MEAN_SERVICE_TIME = 42   # seconds
```

Under these **lightly loaded** conditions, you might see very few tasks waiting in the queue. That is normal if the arrival rate is significantly lower than the system’s total service capacity.

1. **If You Want a Busy System**  
   - **Decrease** the `MEAN_INTERARRIVAL` (increasing arrival rate).  
   - **Decrease** `NUM_COMPUTERS` or **increase** `MEAN_SERVICE_TIME` to reduce capacity.  
   This can cause tasks to queue up and produce a higher average delay time.

2. **If You Want the System to Overload**  
   - Make `MEAN_INTERARRIVAL` even smaller (e.g., 5 seconds).  
   - Reduce the number of computers (e.g., 3 or 4).  
   When \(\lambda\) exceeds total service capacity (\(c \cdot \mu\)), the queue grows large, and average waiting times can become very high.

3. **If You Want a Very Lightly Loaded System**  
   - **Increase** `MEAN_INTERARRIVAL` or **increase** `NUM_COMPUTERS`.  
   - Tasks will rarely queue, and the reported average queue length may be near zero.

---

## Interpreting Results

- **Zero (or Near-Zero) Delays and Queue Length**  
  Indicates that the system is lightly loaded (\(\lambda <\) total service capacity). This is not a bug—it just means the capacity is more than enough to handle arrivals.

- **Large Delay and Waiting Time**  
  Suggests that the arrival rate is close to or exceeds the total service capacity, leading to a busy or overloaded system. You may need more servers or faster service times to reduce congestion.

- **Tasks Processed**  
  If the number of tasks processed is significantly lower or higher than expected, remember the code stops accepting new arrivals at the 5-hour mark (`SIMULATION_TIME = 18000`). Computers may still finish processing tasks that arrived before the cutoff.

---

## Possible Extensions

1. **Fully Event-Driven Simulation**  
   - Include both arrivals and **service completions** as discrete events. This way, the clock can jump to either the next arrival or the next departure, rather than only at arrivals.

2. **Statistical Confidence Intervals**  
   - Run multiple **replications** of the simulation (with different random seeds) and compute confidence intervals for average delay, waiting time, and queue length.

3. **Additional Metrics**  
   - **Server Utilization**: The fraction of time each server (computer) is busy.  
   - **Queue Length Distribution**: Histograms of how many tasks are in the queue over time.  
   - **Maximum Queue Length**: The largest queue length observed within the simulation window.

4. **Alternative Distributions**  
   - Modify `exponential_random` to sample from other distributions (e.g., **Erlang**, **Weibull**, or **Lognormal**) for arrival or service processes.

---

## Troubleshooting

- **No Output or Errors**  
  Make sure you have Python 3.7+ installed and run `python3 simulation.py` from the correct directory.

- **Simulation Takes Too Long or Appears to Hang**  
  If you set a very high arrival rate, the queue can grow large, and the code may need to handle many tasks before reaching the simulation end time.

- **Infinite or Very Large Metrics**  
  If the system is overloaded (\(\lambda\) > total service rate), in theory, the queue length and waiting times can grow unbounded. In practice, you may observe extremely large numbers.

---
## References

- **Gross, D., & Harris, C. M. (2018).** *Fundamentals of Queueing Theory (5th ed.)*. Wiley.  
  - [Wiley Link](https://www.wiley.com/en-us/Fundamentals%2Bof%2BQueueing%2BTheory%2C%2B5th%2BEdition-p-9781118943526)

- **Allen, A. O. (1990).** *Probability, Statistics, and Queueing Theory with Computer Science Applications (2nd ed.)*. Academic Press.  
  - [Internet Archive](https://archive.org/details/probabilitystati0000alle)

- **MIT OpenCourseWare**: Lecture notes on queueing and exponential distributions.  
  - [MIT OCW - Introduction to Probability](https://ocw.mit.edu/courses/res-6-012-introduction-to-probability-spring-2018/)

- **Wikipedia: “Queueing theory.”**  
  - [https://en.wikipedia.org/wiki/Queueing_theory](https://en.wikipedia.org/wiki/Queueing_theory)

These sources cover basic queueing theory (M/M/c queues, exponential arrivals and services, and performance metrics) on which this simulation project is based.

---

## License

This project is licensed under the [MIT License](LICENSE). You are free to modify and distribute the code, provided you include appropriate attribution.
