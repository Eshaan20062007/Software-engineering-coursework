# F536950 25WSA032 Coursework

This repository contains my coursework submission for module 25WSA032 Software Engineering.

## Folder Structure

```
F536950_25WSA032_Coursework/
├── arduino/
│   ├── temperature_optimisation.ino   - Task 2 Arduino code
│   └── temperature_data.csv           - Task 4 recorded data
├── documentation/
│   ├── task4_discussion.md            - Task 4 written discussion
│   └── plot1-5 PNG files              - Task 4 saved figures
├── robots/
│   ├── robot_optimisation.py          - Task 3 simulation code
│   └── task4_analysis.py              - Task 4 analysis script
└── README.md
```

## How to Run

### Task 3 - Robot Simulation

Run from the project root folder:

python robots/robot_optimisation.py

### Task 4 - Temperature Analysis

python robots/task4_analysis.py

This reads the CSV data from `arduino/temperature_data.csv` and produces 5 plots saved to the `documentation/` folder.
