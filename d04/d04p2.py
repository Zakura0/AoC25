with open("input.txt", "r") as f:
    grid = f.read().strip().splitlines()
grid = [[c for c in l] for l in grid]

height = len(grid)
width = len(grid[0])

result = 0
removable = set()
while True:
    for r in range(height):
        for c in range(width):
            if grid[r][c] == "@":
                count = 0
                for d in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    if r + d[0] >= 0 and r + d[0] < height and c + d[1] >= 0 and c + d[1] < width:
                        if grid[r + d[0]][c + d[1]] == "@":
                            count += 1
                if count < 4:
                    removable.add((r, c))
    if not removable:
        break
    for r, c in removable:
        grid[r][c] = "."
        result += 1
    removable.clear()

print(result)
