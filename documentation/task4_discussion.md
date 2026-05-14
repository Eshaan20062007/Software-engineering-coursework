# Task 4 - Discussion of Results

## Time-domain behaviour (Plot 1 and Plot 3)

The temperature was steady for a couple of seconds at about 23.3C but then it suddenly increased to about 25C due to me warming it up with my hands. The smoothed plot shows this more clearly because it got rid of the small changes between readings. The signal appeared mostly stable with only minor noise between consecutive readings.

## Frequency-domain behaviour (Plot 2)

The magnitude vs frequency plot shows a large spike at the beginning which corresponds to the sudden change in temperature when I warmed it up with my hands. After the initial spike the magnitude drops and stays low which means the temperature was not changing rapidly or periodically. This makes sense because the temperature of the room was mostly stable.

## System behaviour (Plot 5)

The Arduino correctly switched to IDLE and POWER DOWN mode because the temperature was stable for most of the recording. This shows that the system is working as intended to save power when the temperature is fairly constant. One improvement would be to increase the number of readings to cover a longer period of time, which would better capture the trends in temperature.

## Data quality (Plot 4)

The 3 minute recording was enough to capture the temperature changes in the room. The 1 second sampling rate was appropriate for room temperature monitoring because the temperature is unlikely to change much in a second. One limitation is that the Arduino memory only allowed for a certain number of readings which limited the time of the recording.
