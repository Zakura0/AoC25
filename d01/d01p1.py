with open ("input.txt") as f:
    directions = f.read().strip().split("\n")

dial_value = 50
count = 0

for d in directions:
    rotation = d[0]
    value = int(d[1:])
    if d[0] == "R":
        dial_value += value
    else:
        dial_value -= value
    dial_value %= 100
    if dial_value == 0:
        count += 1

print(count)