with open("input.txt", "r") as f:
    machines = f.read().strip().splitlines()

result = 0

for i, machine in enumerate(machines):
    config = machine.split(" ")[-1][1:-1]
    config = list(map(int, config.split(",")))
    counters = [0] * len(config)
    buttons = machine.split(" ")[1:-1]
    buttons = [list(map(int, button[1:-1].split(","))) for button in buttons]


