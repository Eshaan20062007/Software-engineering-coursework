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
plt.xlabel('Time (seconds)')
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

# Discussion of results:

# Time-domain behaviour (Plot 1 and Plot 3)
# The temperature was steady for a couple seconds at about 23.3C
# but then it suddenly incrased to about 25C due to me warming it up with my hands.
# The smoothed plot shows this more clearly because it got rid of small
# changes between readings. The signal appeared mostly stable with
# only minor noise between consecutive readings.

# Frequency-domain behaviour (Plot 2)
# The magnitude vs frequency plot shows a large spike at the beginning
# which corresponds to the sudden change in temperature when I warmed it up with my hands.
# After the initial spike the magnitude drops and stays low which means
# the temperature was not changing rapidly or periodically.
# This makes sense because the temperature of the room was mostly stable

# System behaviour
# The Arduino correctly switched to IDLE and POWER DOWN mode because the temperature
# was stable for most of the recording.
# This shows that the system is working as intended to save power 
# when the temperature is fairly constant.
# One improvement would be to increase the number of readings to cover
# a longer period of time, which would better capture the trends in temperature

# Data quality
# The 3 minute recording was enough to capture the temperature changes in the room
# The 1 second sampling rate was appropriate for room temperature monitoring
# because the temperature is unlikely to change much in a second.
# One limitation is that the Arduino memory only allowed for a certain number of readings
# which limited the time of the recording.