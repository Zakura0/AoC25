with open ("input.txt") as f:
    blocks = f.read().strip().split("\n\n")

ranges = [tuple(map(int, b.split("-"))) for b in blocks[0].splitlines()]
ranges.sort(key=lambda x: x[0])
result = 0
merged = []
for range in ranges:
    lower, upper = range
    if merged and lower <= merged[-1][1] + 1:
        merged[-1] = (merged[-1][0], max(merged[-1][1], upper))
    else:
        merged.append((lower, upper))
ranges = merged

for range in ranges:
    lower, upper = range
    result += upper + 1 - lower

print(result)
