import numpy as np

with open("sample.txt", "r") as f:
    machines = f.read().strip().splitlines()

result = 0

for i, machine in enumerate(machines):
    config = machine.split(" ")[-1][1:-1]
    config = list(map(int, config.split(",")))
    v_config = np.array(config)
    counters = [0] * len(config)
    buttons = machine.split(" ")[1:-1]
    buttons = [list(map(int, button[1:-1].split(","))) for button in buttons]
    b_buttons = []
    for b in buttons:
        b_button = np.zeros(v_config.shape[0])
        for pos in b:
            b_button[pos] = 1
        b_buttons.append(b_button)
    b_buttons = np.array(b_buttons)
    print(np.linalg.lstsq(b_buttons.T, v_config, rcond=None)[0])



