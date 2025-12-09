import os
os.chdir(os.path.dirname(__file__))

with open("input.txt", "r") as f:
    reds = [tuple(map(int, l.split(","))) for l in f.read().strip().splitlines()]

edges = []

for i in range(len(reds) - 1):
    red1x, red1y = reds[i]
    red2x, red2y = reds[i+1]
    edges.append((red1x, red1y, red2x, red2y))

edges.append((reds[0][0], reds[0][1], reds[-1][0], reds[-1][1]))

def intersects(minx, miny, maxx, maxy):
    for e in edges:
        x1, y1, x2, y2 = e
        minx_e = min(x1, x2)
        maxx_e = max(x1, x2)
        miny_e = min(y1, y2)
        maxy_e = max(y1, y2)
        if minx < maxx_e and maxx > minx_e and miny < maxy_e and maxy > miny_e:
            return True
    return False

valid = []

for i, red1 in enumerate(reds):
    for red2 in reds[i+1:]:
        a1, b1 = red1
        a2, b2 = red2
        minx = min(a1, a2)
        maxx = max(a1, a2)
        miny = min(b1, b2)
        maxy = max(b1, b2)
        if not intersects(minx, miny, maxx, maxy):
            area = (abs(a1 - a2) + 1) * (abs(b1 - b2) + 1)
            valid.append((area, red1, red2))

valid.sort(reverse=True)
print(valid[0][0])
        