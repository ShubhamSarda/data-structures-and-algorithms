import time
time.time()

timestamp1 = time.time()

# Sum of natural numbers up to num
num = 100
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)

### Program Completed ###

timestamp2 = time.time()
print((timestamp2 - timestamp1))