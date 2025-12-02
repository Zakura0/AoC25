with open ("input.txt") as f:
    ranges = [tuple(map(int, r.split("-"))) for r in f.read().strip().split(",")]

result = 0

for (rs, re) in ranges:
    for i in range(rs, re + 1):
        stri = str(i)
        vlen = len(stri)
        ls = ""
        found = False
        for j in range(1, vlen):
            if found:
                break
            if stri[:j] in stri[j:]:
                ls = stri[:j]
                x = 2
                while True and not ls == "":
                    if ls * x == stri:
                        result += i
                        found = True
                        break
                    if len(ls * x) > vlen:
                        break
                    x += 1
            else:
                break
print(result)


            