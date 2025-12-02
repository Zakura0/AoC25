import time

start_time = time.perf_counter()

with open ("input.txt") as f:
    ranges = [tuple(map(int, r.split("-"))) for r in f.read().strip().split(",")]

result = 0

for (rs, re) in ranges:
    for i in range(rs, re + 1):
        if len(str(i)) % 2 == 0:
            if int(str(i)[:(len(str(i))//2)]) == int(str(i)[(len(str(i))//2):]):
                result += i

print(result)

end_time = time.perf_counter()
runtime = end_time - start_time
print(f"Runtime: {runtime*1000:.3f} ms ({runtime:.6f} seconds)")