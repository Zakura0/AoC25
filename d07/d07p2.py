from functools import cache

with open("input.txt", "r") as f:
    grid = f.read().strip().splitlines()

grid = [[c for c in l] for l in grid]

height = len(grid)
width = len(grid[0])

start = (0, 0)

for r in range(height):
    for c in range(width):
        if grid[r][c] == "S":
            start = (r, c)
@cache
def go(r, c):
    if r+1 >= height:
        return 1
    if grid[r+1][c] == ".":
        return go(r+1, c)
    if grid[r+1][c] == "^":
        return go(r+1, c-1) + go(r+1, c+1)

print(go(start[0], start[1]))
