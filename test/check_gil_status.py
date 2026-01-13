from threading import Thread
import time
import sys


def task(i):
    print(f"task {i} is running")
    total = 0
    for _ in range(100_000_000):  # ← 1亿次
        total += 1
    print(f"task {i} is done")


def single_thread():
    start_time = time.time()
    for i in range(3):
        task(i)
    end_time = time.time()
    print(f"total time used: {end_time - start_time}")


def multi_thread():
    start_time = time.time()
    threads = []
    for i in range(3):
        t = Thread(target=task, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    end_time = time.time()
    print(f"total time used: {end_time - start_time}")


def main():
    print(f"Python version: {sys.version}")
    if 'free-threading' in sys.version:
        print('gil disabled')
    else:
        print('gil disabled')
    print("Single thread test:")
    single_thread()
    print("Multi thread test:")
    multi_thread()


if __name__ == "__main__":
    main()
