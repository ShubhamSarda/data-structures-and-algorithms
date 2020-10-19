import time
time.time()

timestamp1 = time.time()

### Python Program to find Sum of N Natural Numbers ###
number = 100
total = 0

for value in range(1, number + 1):
    total = total + value

print("The sum is", total)

### Program Completed ###

timestamp2 = time.time()
print((timestamp2 - timestamp1))