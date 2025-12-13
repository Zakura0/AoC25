with open("input.txt", "r") as f:
    connections = f.read().strip().splitlines()

devices = {}
for connection in connections:
    node, neighbors = connection.split(": ")
    devices[node] = neighbors.split()

cache = {}

def count_paths(devices, start, fft, dac):
    if start == "fft":
        fft = True
    if start == "dac":
        dac = True        
    if start == "out":
        if fft and dac:
            return 1
        return 0
    
    key = (start, fft, dac)
    if key in cache:
        return cache[key]
    
    total = 0
    for neighbor in devices[start]:
        total += count_paths(devices, neighbor, fft, dac)
    
    cache[key] = total
    return total

result = count_paths(devices, "svr", False, False)
print(result)

    
