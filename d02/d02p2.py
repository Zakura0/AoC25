with open ("input.txt") as f:
    ranges = [tuple(map(int, r.split("-"))) for r in f.read().strip().split(",")]


