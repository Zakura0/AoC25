with open ("input.txt") as f:
    banks = f.read().strip().splitlines()

result = 0

for b in banks:
    largest = "0"
    for j in b:
        if b.index(j) == len(b) - 1:
            break
        if int(j) > int(largest):
            largest = j
    index = b.index(largest)
    second_largest = "0"
    for i in range(index + 1, len(b)):
        if int(b[i]) > int(second_largest):
            second_largest = b[i]

    result += int(str(largest) + str(second_largest))

print(result)

