from collections import Counter


left_arr = []
right_arr = []

with open("day-01/input.txt") as f:
    lines = f.readlines()
    for line in lines:
        left, right = line.split()
        left_arr.append(int(left))
        right_arr.append(int(right))

right_frequency = Counter(right_arr)

similarity_score = 0
for left in left_arr:
    similarity_score += left * right_frequency[left]

print(similarity_score)