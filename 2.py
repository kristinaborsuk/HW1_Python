seconds = int(input("Seconds:"))
seconds_in_hour = 60 * 60
wasted_hours = seconds // seconds_in_hour
if wasted_hours:
    seconds -= wasted_hours * 60 * 60
    print(f"Result: {seconds}")
else:
    print(f"Result: {0}")