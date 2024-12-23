# ACPC Grading System Server Simulation

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

