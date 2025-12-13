with open("input.txt", "r") as f:
    blocks = f.read().strip().split("\n\n")

shapes = {}
regions = []

result = 0

for i in range(5):
    lines = blocks[i].split("\n")
    grid = [list(line) for line in lines[1:]]
    shapes[i] = grid

lines = blocks[-1].split("\n")
for line in lines:
    parts = line.split()
    size = parts[0][:-1].split("x")
    height, width = int(size[0]), int(size[1])
    values = [int(x) for x in parts[1:]]
    regions.append((height, width, *values))


for region in regions:
    if region[0] * region[1] >= sum(region[2:]) * 9:
        result += 1

print(result)
    



