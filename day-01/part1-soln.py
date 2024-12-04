left_arr = []
right_arr = []

with open("day-01/input.txt") as f:
    lines = f.readlines()
    for line in lines:
        left, right = line.split()
        left_arr.append(int(left))
        right_arr.append(int(right))

left_arr.sort()
right_arr.sort()

sum=0
for a,b in zip(left_arr, right_arr):
    sum += abs(a-b)

print(sum)

