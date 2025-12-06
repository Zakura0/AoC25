with open("input.txt", "r") as f:
    lines = [l for l in f.read().strip("\n").splitlines()]
columns = list(zip(*lines))

result = 0
operation = columns[0][-1]
block_result = 0
block = []
for c in columns:
    if c[-1] != " ":
        operation = c[-1]
    if set(c) == {" "}:
        result += eval(operation.join(block))
        block = []
    else:
        block.append(("".join(c[:-1])).strip())

result += eval(operation.join(block))
print(result)


    
    