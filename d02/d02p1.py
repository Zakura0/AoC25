with open ("input.txt") as f:
    ranges = [tuple(map(int, r.split("-"))) for r in f.read().strip().split(",")]

result = 0

for (rs, re) in ranges:
    for i in range(rs, re + 1):
        stri = str(i)
        vlen = len(stri)
        if vlen % 2 == 0:
            if int(stri[:(vlen//2)]) == int(stri[(vlen//2):]):
                result += i

print(result)