import time

hours = int(input("Enter total hours: "))
minutes = int(input("Enter total minutes: "))
seconds = int(input("Enter total seconds: "))

my_time = hours * 3600 + minutes * 60 + seconds

for x in range(my_time, 0, -1):
    second = x % 60
    minute = int(x / 60) % 60
    hour = int(x / 3600) % 60
    print(f"{hour:02}:{minute:02}:{second:02}")
    time.sleep(1)

print("Time's up")