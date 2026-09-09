# Write a python program to print numbers from 1 to 50, but skip all numbers divisible by 4.
for i in range(1,51):
    if i%4==0:
        continue
    print(i)