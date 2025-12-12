with open("samplep2.txt", "r") as f:
    connections = f.read().strip().splitlines()

devices = {}
for connection in connections:
    node, neighbors = connection.split(": ")
    devices[node] = neighbors.split()

def find_all_paths(devices, start, path):
    if start == "out":
        if "fft" in path and "dac" in path:
                return 1
        return 0            
    path = path + [start]
    paths = 0
    for neighbor in devices[start]:
        if neighbor not in path:
            new_path = find_all_paths(devices, neighbor, path)
            paths += new_path
    return paths

all_paths = find_all_paths(devices, "svr", [])
print(all_paths)

    
