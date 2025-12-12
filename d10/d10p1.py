with open("input.txt", "r") as f:
    machines = f.read().strip().splitlines()

result = 0

def find_shortest_path(config, lights, buttons):
    queue = [(lights, [])]
    visited = {lights}
    
    while queue:
        current, path = queue.pop(0)
        
        if current == config:
            return path
        
        for button in buttons:
            next_lights = list(current)
            for light_pos in button:
                if 0 <= light_pos < len(next_lights):
                    if next_lights[light_pos] == '.':
                        next_lights[light_pos] = '#'
                    else:
                        next_lights[light_pos] = '.'
            next_lights = "".join(next_lights)
            
            if next_lights not in visited:
                visited.add(next_lights)
                queue.append((next_lights, path + [button]))

for machine in machines:
    config = machine.split(" ")[0][1:-1]
    lights = "".join("."*len(config))
    buttons = machine.split(" ")[1:-1]
    buttons = [list(map(int, button[1:-1].split(","))) for button in buttons]

    path = find_shortest_path(config, lights, buttons)
    result += len(path)

print(result)


