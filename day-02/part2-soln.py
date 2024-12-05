reports = []
safe_count = 0

# CODE IS SHIT, REFACTOR IT!!!
with open('day-02/input.txt') as f:
    for line in f.readlines():
        report = list(map(int, line.split()))

        for skip_index in range(len(report)):
            prev = None

            desc = False
            asc = False

            for i in range(len(report)):
                if i == skip_index:
                    continue

                curr = report[i]

                if prev is None:
                    prev = curr
                    continue

                if prev < curr:
                    asc = True
                elif prev > curr:
                    desc = True

                if abs(curr - prev) > 3 or curr==prev or (asc and desc):
                    break

                prev = curr

            else:
                safe_count+=1
                break
            
print(safe_count)