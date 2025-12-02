# import sys
# sys.path.append('..')
# import timer

import time
start_time = 0

def start():
    global start_time
    start_time = time.perf_counter()

def stop():
    global start_time
    end_time = time.perf_counter()
    runtime = end_time - start_time
    print(f"Runtime: {runtime*1000:.3f} ms ({runtime:.6f} seconds)")