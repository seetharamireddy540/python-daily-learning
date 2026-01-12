import threading
import time


def worker(name, delay):
    print(f"Thread {name} started")
    time.sleep(delay)
    print(f"Thread {name} finished")


thread1 = threading.Thread(target=worker, args=("Thread 1", 2))
thread2 = threading.Thread(target=worker, args=("Thread 2", 5))
thread3 = threading.Thread(target=worker, args=("Thread 3", 1))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("All threads completed")
