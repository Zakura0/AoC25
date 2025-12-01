import time

start_time = time.perf_counter()

with open ("input.txt") as f:
    directions = f.read().strip().split("\n")

dial_value = 50
clicks = 0

for d in directions:
    rotation = d[0]
    value = int(d[1:])
    full_circles = value // 100
    prev = dial_value
    if rotation == "R":
        dial_value = (dial_value + value) % 100
        if prev > dial_value:
            clicks += 1
    else:
        dial_value = (dial_value - value) % 100
        if (prev > dial_value and dial_value == 0) or (prev < dial_value and prev != 0): #PAIN
            clicks += 1
    clicks += full_circles
    if dial_value == 0:
        continue

print(clicks)

end_time = time.perf_counter()
runtime = end_time - start_time
print(f"Runtime: {runtime*1000:.3f} ms ({runtime:.6f} seconds)")


