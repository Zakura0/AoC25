with open("input.txt", "r") as f:
    machines = f.read().strip().splitlines()

result = 0

def find_shortest_path(config, counters, buttons):
    queue = [(counters, [])]
    visited = {tuple(counters)}
    
    while queue:
        current, path = queue.pop(0)
        
        if current == config:
            return path
        
        for button in buttons:
            next_counters = list(current)
            for counter_pos in button:
                if 0 <= counter_pos < len(next_counters):
                    next_counters[counter_pos] += 1
            
            if tuple(next_counters) not in visited:
                visited.add(tuple(next_counters))
                queue.append((next_counters, path + [button]))

for i, machine in enumerate(machines):
    print(f"Processing Machine {i} of {len(machines)}")
    config = machine.split(" ")[-1][1:-1]
    config = list(map(int, config.split(",")))
    counters = [0] * len(config)
    buttons = machine.split(" ")[1:-1]
    buttons = [list(map(int, button[1:-1].split(","))) for button in buttons]

    path = find_shortest_path(config, counters, buttons)
    result += len(path)

print(result)


