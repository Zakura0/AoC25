with open ("input.txt") as f:
    blocks = f.read().strip().split("\n\n")

ranges = blocks[0].splitlines()
ids = blocks[1].splitlines()

result = 0

for id in ids:
    for range in ranges:
        lower, upper = map(int, range.split("-"))
        if int(id) >= lower and int(id) <= upper:
            result += 1
            break

print(result)