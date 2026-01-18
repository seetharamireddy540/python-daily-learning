import threading
import multiprocessing
import time


# CPU-bound task (calculation)
def cpu_bound_task(n):
    total = 0
    for i in range(n):
        total += i * i
    return total


# I/O-bound task (simulated with sleep)
def io_bound_task(duration):
    print(f"Starting I/O task for {duration} seconds")
    time.sleep(duration)
    print("I/O task completed")


# Threading example (good for I/O-bound)
def threading_example():
    threads = []
    start = time.time()

    for i in range(40):
        t = threading.Thread(target=io_bound_task, args=(1,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"Threading took: {time.time() - start:.2f} seconds")


# Multiprocessing example (good for CPU-bound)
def multiprocessing_example():
    start = time.time()

    with multiprocessing.Pool(40) as pool:
        pool.map(cpu_bound_task, [1000000] * 4)

    print(f"Multiprocessing took: {time.time() - start:.2f} seconds")


if __name__ == "__main__":
    threading_example()
    multiprocessing_example()
