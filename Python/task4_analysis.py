# task4_analysis.py
# Task 4 - Temperature Data Analysis and Visualisation

import matplotlib.pyplot as plt
import math

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
plt.plot(time_values, temperature_values, marker = '.')
plt.title('Temperature vs Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Temperature (C)')
plt.grid(True)
plt.show()

# Calculate the DFT manually the same way as the Arduino code
n = len(temperature_values)
magnitude = []
frequency = []

for k in range(n):
    real = 0
    imag = 0
    for i in range(n):
        real += temperature_values[i] * math.cos(2 * math.pi * k * i / n)
        imag -= temperature_values[i] * math.sin(2 * math.pi * k * i / n)
    magnitude.append(math.sqrt(real**2 + imag**2))
    frequency.append(k / n)  # frequency in Hz

plt.figure()
plt.plot(frequency, magnitude)
plt.title('Magnitude vs Frequency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()

# Calculate a moving average with a window of 10 readings
window = 10
smoothed = []

for i in range(len(temperature_values)):
    # For the first few readings use whatever readings are available
    start = max(0, i - window)
    average = sum(temperature_values[start:i+1]) / len(temperature_values[start:i+1])
    smoothed.append(average)

# Plot both the original and smoothed temperature on the same graph
plt.figure()
plt.plot(time_values, temperature_values, marker='.', label='Original')
plt.plot(time_values, smoothed, label='Smoothed')
plt.title('Smoothed Temperature vs Time')
plt.ylabel('Temperature (C)')
plt.legend()
plt.grid(True)
plt.show()

# Plot the histogram of temperature values
plt.figure()
plt.hist(temperature_values, bins=10)
plt.title('Histogram of Temperature Readings')
plt.xlabel('Temperature (C)')
plt.ylabel('Number of Readings')
plt.grid(True)
plt.show()

# Plot temperature change rate vs time

# Calculate the difference between each consecutive temperature reading
change_rate = []
change_time = []

for i in range(1, len(temperature_values)):
    change = temperature_values[i] - temperature_values[i-1]
    change_rate.append(change)
    change_time.append(time_values[i])

plt.figure()
plt.plot(change_time, change_rate, marker='.')
plt.title('Temperature Change Rate vs Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Temperature Change (C per second)')
plt.grid(True)
plt.show()