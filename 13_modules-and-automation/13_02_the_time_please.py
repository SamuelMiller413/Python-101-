# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.

import datetime as dt

current_date = dt.date.today()
current_time = dt.datetime.now()

print(f"Date - {current_date.month}-{current_date.day}-{current_date.year}")
print(f"Time - {current_time.hour}:{current_time.minute}")
