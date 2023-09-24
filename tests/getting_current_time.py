import time

# Get the current time in seconds
ct_seconds = time.time()
# Convert the seconds
ct_object = time.localtime(ct_seconds)

# Invoking values
current_hour, current_minute, current_second = ct_object.tm_hour, ct_object.tm_min, ct_object.tm_sec

print(f"Current Time: {current_hour:02}:{current_minute:02}:{current_second:02}")
