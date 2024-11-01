from datetime import time

time_1 = time(hour=8, minute=0)
print(time_1)
time_2 = time_1.strftime("%H:%M")
print(time_2)