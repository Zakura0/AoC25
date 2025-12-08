from math import dist, prod

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
circuits = [[distances[0][1], distances[0][2]]]

for i in range(1, 1000):
    connected = False
    box1, box2 = distances[i][1], distances[i][2]
    for circuit in circuits:
        if box1 in circuit and box2 in circuit:
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

circuits.sort(key = lambda x: len(x), reverse=True)
print(prod([len(c) for c in circuits[:3]]))




    

