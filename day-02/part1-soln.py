reports = []
safe_count = 0
with open('day-02/input.txt') as f:
    for line in f.readlines():
        report = list(map(int, line.split()))

        increasing = report[1] > report[0]

        for i in range(1, len(report)):
            if abs(report[i] - report[i-1]) > 3:
                break

            if increasing and report[i] <= report[i-1]:
                break

            if not increasing and report[i] >= report[i-1]:
                break
        else:
            safe_count+=1
            
print(safe_count)