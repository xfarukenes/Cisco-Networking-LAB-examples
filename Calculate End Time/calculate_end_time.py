hour = int(input("Staring time (hours): "))
minute = int(input("Starting time (minutes): "))
duration = int(input("Event duration (minutes): "))

# Calculate the end time
total_minutes = minute + duration
end_hour = hour + total_minutes // 60

end_minute = total_minutes % 60
end_hour = end_hour % 24  # Wrap around if more than 24 hours
print(f"End time: {end_hour}:{end_minute}")