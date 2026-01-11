import sys
import threading
import time
import math


def cpu_intensive_task(n):
    """更复杂的CPU密集型任务，用于测试GIL的影响"""
    result = 0
    for i in range(n):
        # 更复杂的数学运算
        result += math.sqrt(i) * math.sin(i) * math.cos(i)
        # 增加质数计算
        if i > 1 and i % 100000 == 0:
            is_prime = True
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    is_prime = False
                    break
    return result


def single_thread_test(task_size):
    """单线程执行任务"""
    print("Running single thread test...")
    start_time = time.time()

    # 执行四次相同的计算任务
    result1 = cpu_intensive_task(task_size)
    result2 = cpu_intensive_task(task_size)
    result3 = cpu_intensive_task(task_size)
    result4 = cpu_intensive_task(task_size)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Single thread completed in {execution_time:.2f} seconds")
    return execution_time


def multi_thread_test(task_size):
    """多线程执行任务"""
    print("Running multi-thread test...")
    start_time = time.time()

    # 创建四个线程分别执行计算任务
    results = [None, None, None, None]

    def worker(index):
        results[index] = cpu_intensive_task(task_size)

    # 启动线程
    threads = []
    for i in range(4):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Multi-thread completed in {execution_time:.2f} seconds")
    return execution_time


def cpu_bound_multithreading():
    """测试CPU密集型任务的多线程效果"""
    print("=" * 60)
    print("Python GIL 对 CPU 密集型多线程任务的影响测试")
    print("=" * 60)
    print(f"Python version: {sys.version}")
    print()

    # 设置更大的计算任务大小以增加差异化
    task_size = 5000000

    # 执行单线程测试
    single_time = single_thread_test(task_size)
    print()

    # 执行多线程测试
    multi_time = multi_thread_test(task_size)
    print()

    # 分析结果
    print("结果分析:")
    print(f"单线程执行时间: {single_time:.2f} 秒")
    print(f"多线程执行时间: {multi_time:.2f} 秒")

    # 计算加速比
    if multi_time > 0:
        speedup = single_time / multi_time
        print(f"加速比: {speedup:.2f}x")

    # 判断GIL影响
    print()
    if multi_time > single_time * 0.7:
        print("结论: GIL对CPU密集型任务有显著影响")
        print("多线程在CPU密集型任务中没有明显性能提升")
    else:
        print("结论: GIL对当前环境影响较小")
        print("多线程能够有效提升CPU密集型任务性能")

    # 额外分析
    theoretical_best = single_time / 4
    print(f"\n理论最佳时间(4核并行): {theoretical_best:.2f} 秒")
    print(f"实际多线程时间: {multi_time:.2f} 秒")
    efficiency = (theoretical_best / multi_time) * 100 if multi_time > 0 else 0
    print(f"并行效率: {efficiency:.1f}%")


if __name__ == "__main__":
    cpu_bound_multithreading()
