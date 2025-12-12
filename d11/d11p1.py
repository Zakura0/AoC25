with open("input.txt", "r") as f:
    connections = f.read().strip().splitlines()

devices = {}
for connection in connections:
    node, neighbors = connection.split(": ")
    devices[node] = neighbors.split()

def find_all_paths(devices, start, path):
    if start == "out":
            return [path + ["out"]]
    path = path + [start]
    paths = []
    for neighbor in devices[start]:
        if neighbor not in path:
            new_path = find_all_paths(devices, neighbor, path)
            paths.extend(new_path)
    return paths

all_paths = find_all_paths(devices, "you", [])
# for path in all_paths:
#     print(" -> ".join(path))
print(len(all_paths))

    
