import time

start_time = time.perf_counter()

with open ("input.txt") as f:
    directions = f.read().strip().split("\n")

dial_value = 50
zero_clicks = 0

for d in directions:
    rotation = d[0]
    value = int(d[1:])
    for i in range(0, value):
        if rotation == "R":
            dial_value = (dial_value + 1) % 100
            if dial_value == 0:
                zero_clicks += 1
        else:
            dial_value = (dial_value - 1) % 100
            if dial_value == 0:
                zero_clicks += 1

print(zero_clicks)

end_time = time.perf_counter()
runtime = end_time - start_time
print(f"Runtime: {runtime*1000:.3f} ms ({runtime:.6f} seconds)")