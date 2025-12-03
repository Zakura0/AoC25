with open ("input.txt") as f:
    banks = f.read().strip().splitlines()

result = 0

for bank in banks:
    spaces = 12
    joltage = ""
    for i in range(spaces - 1, -1, -1):
        largest = 0
        for j in bank:
            if int(j) > largest and len(bank[bank.index(j) + 1:]) >= i:
                largest = int(j)
        joltage += str(largest)
        if i > 0:
            bank = bank[bank.index(str(largest)) + 1:]
    result += int(joltage)
print(result)


        

        

    