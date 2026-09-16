import time
from decay import simulate

start = time.perf_counter()
simulate(200000, 0.4)
end = time.perf_counter()

print(f"Time taken: {end - start:.5f} seconds")