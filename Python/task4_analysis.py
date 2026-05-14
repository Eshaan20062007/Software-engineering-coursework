# task4_analysis.py
# Task 4 - Temperature Data Analysis and Visualisation

import matplotlib.pyplot as plt

# Load the data form the CSV file
# Create empty lists to store the data
time_values = []
temperature_values = []

# Open the CSV file and read it line by line
with open(r'C:\Users\evfir\OneDrive - Loughborough University\Visual studio code\Software-engineering-coursework\arduino\temperature_data.csv', 'r') as file:
    for line in file:

        # Split by comma to separate time and temperature
        parts = line.strip().split(',')

        # Extract the number after "time: "
        time = float(parts[0].split(':')[1])

        # Extract the number after "temperature: "
        temperature = float(parts[1].split(':')[1])

        time_values.append(time)
        temperature_values.append(temperature)

print(f"Loaded {len(time_values)} readings")

# plot temperature vs time
plt.figure()
plt.plot(time_values, temperature_values)
plt.title('Temperature vs Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Temperature (C)')
plt.grid(True)
plt.show()