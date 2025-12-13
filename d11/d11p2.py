with open("samplep2.txt", "r") as f:
    connections = f.read().strip().splitlines()

devices = {}
for connection in connections:
    node, neighbors = connection.split(": ")
    devices[node] = neighbors.split()
    def find_all_paths(devices, start, path, fft, dac):
        if start == "fft":
            fft = True
        if start == "dac":
            dac = True        
        if start == "out":
            if fft and dac:
                return [path + ["out"]]
            else:
                return []
        
        path = path + [start]
        paths = []
        for neighbor in devices[start]:
            if neighbor not in path:
                new_path = find_all_paths(devices, neighbor, path, fft, dac)
                paths.extend(new_path)
        return paths

all_paths = find_all_paths(devices, "svr", [], False, False)
print(len(all_paths))

    
