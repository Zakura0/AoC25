from math import dist

with open("input.txt", "r") as f:
    boxes = [tuple(map(int, l.split(","))) for l in f.read().strip().splitlines()]

distances = []
checked = []

for b1 in boxes:
    for b2 in boxes:
        if b1 == b2 or b2 in checked:
            continue
        distance = dist(b1, b2)
        data = (distance, b1, b2)
        distances.append(data)
    checked.append(b1)

distances.sort()
circuits = []

x_coords = (0,0)
i = 0
while True:
    box1, box2 = distances[i][1], distances[i][2]
    connected = False
    for circuit in circuits:
        if (box1 in circuit and box2 in circuit):
            break
        if box1 in circuit:
            for c in circuits:
                if c == circuit:
                    continue
                if box2 in c:
                    circuits.append([*circuit, *c])
                    circuits.remove(circuit)
                    circuits.remove(c)
                    connected = True
                    break
            else:
                circuit.append(box2)
                break
        elif box2 in circuit:
            for c in circuits:
                if c == circuit:
                    continue
                if box1 in c:
                    circuits.append([*circuit, *c])
                    circuits.remove(circuit)
                    circuits.remove(c)
                    connected = True
                    break
            else:
                circuit.append(box1)
                break
        if connected:
            break
    else:
        circuits.append([box1, box2])

    x_coords = (box1[0], box2[0])

    if len(circuits) == 1 and len(circuits[0]) == len(boxes):
        break
    
    i += 1

circuits.sort(key = lambda x: len(x), reverse=True)
print(x_coords[0] * x_coords[1])




    

