import time

my_time = int(input("Enter the time in the second: ")) #90

for x in range(my_time,0,-1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hour = int(x / 3600)
    print(f"{hour:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME's UP")