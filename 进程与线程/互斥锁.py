# 使用互斥锁完成2个线程对同一个全局变量各加100万次的操作
# 两种方式实现：join方法和互斥锁
import threading


# 定义全局变量
g_num = 0


# 创建互斥锁,Lock本身是一个函数，通过调用函数可以创建一把互斥锁
lock = threading.Lock()


# 循环100完成执行的任务
def task1():
    # 上锁
    lock.acquire()
    for i in range(1000000):
        # 每循环一次给全局变量加1
        global g_num  # 声明修改全局变量的内存地址
        g_num += 1

    # 数据计算完成
    print("task1:", g_num)
    # 释放锁
    lock.release()


def task2():
    # 上锁
    lock.acquire()
    for i in range(1000000):
        # 每循环一次给全局变量加1
        global g_num  # 声明修改全局变量的内存地址
        g_num += 1

    # 数据计算完成
    print("task2:", g_num)
    # 释放锁
    lock.release()


if __name__ == '__main__':
    # 创建两个子进程
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)

    # 启动线程执行任务
    first_thread.start()
    # 使用线程等待join()
    # first_thread.join()
    second_thread.start()
