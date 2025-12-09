with open("input.txt", "r") as f:
    edges = [tuple(map(int, l.split(","))) for l in f.read().strip().splitlines()]

rectangles = []
amount = len(edges)

for i, edge1 in enumerate(edges):
    for edge2 in edges[i:]:
        a1, b1 = edge1
        a2, b2 = edge2
        area = (abs(a1 - a2) + 1) * (abs(b1 - b2) + 1)
        rectangles.append((area, edge1, edge2))

rectangles.sort(reverse=True)
print(rectangles[0][0])
