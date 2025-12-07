with open("input.txt", "r") as f:
    grid = f.read().strip().splitlines()
grid = [[c for c in l] for l in grid]

height = len(grid)
width = len(grid[0])

beams = []
seen = set()

for r in range(height):
    for c in range(width):
        if grid[r][c] == "S":
            seen.add((r+1,c))
            beams.append((r+1,c))

result = 0

while beams:
    row, col = beams.pop()
    if row + 1 >= height:
        continue
    if grid[row + 1][col] == "^":
        split = False
        for d in [-1, 1]:
            if (row + 1, col + d) not in seen:
                split = True
                beams.append((row + 1, col + d))
                seen.add((row + 1, col + d))
        if split:
            result += 1
    else:
        beams.append((row+1,col))
        seen.add((row+1,col))

print(result)



        