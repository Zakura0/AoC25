with open("input.txt", "r") as f:
    grid = f.read().strip().splitlines()

columns = list(zip(*[row.split() for row in grid]))

result = 0

for c in columns:
    res = 0
    for num in c[:-1]:
        if c[-1] == "*":
            if res == 0:
                res += 1
            res *= int(num) 
        else :
            res += int(num) 
    result += res

print(result)

