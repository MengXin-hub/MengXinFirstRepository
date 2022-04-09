# 1、导入进程包
import multiprocessing
import time
import os


# 跳舞任务
def dance():
    # 获取当前进程（子进程）编号
    dance_process_id = os.getpid()
    # 获取当前进程对象，查看当前代码是由哪个进程执行的：multiprocessing.current_process()
    print("dance_process_id:", dance_process_id, multiprocessing.current_process())
    # 获当前进程的父进程编号
    dance_process_parent_id = os.getppid()
    print("dance_process的父进程编号是:", dance_process_parent_id)

    for i in range(3):
        print("跳舞中···")
        time.sleep(0.2)
        # 根据进程编号杀强行死指定进程
        os.kill(dance_process_id, 9)


# 唱歌任务
def sing():
    # 获取当前进程（子进程）编号
    sing_process_id = os.getpid()
    # 获取当前进程对象，查看当前代码是由哪个进程执行的：multiprocessing.current_process()
    print("sing_process_id:", sing_process_id, multiprocessing.current_process())
    # 获当前进程的父进程编号
    sing_process_parent_id = os.getppid()
    print("sing_process的父进程编号是:", sing_process_parent_id)

    for i in range(3):
        print("唱歌中···")
        time.sleep(0.2)


if __name__ == "__main__":
    """
    RuntimeError: 
        An attempt has been made to start a new process before the
        current process has finished its bootstrapping phase.

        This probably means that you are not using fork to start your
        child processes and you have forgotten to use the proper idiom
        in the main module:

            if __name__ == '__main__':
                freeze_support()
                ...

        The "freeze_support()" line can be omitted if the program
        is not going to be frozen to produce an executable.
    """

    # 获取当前进程（主进程）编号
    main_process_id = os.getpid()
    # 获取当前进程对象，查看当前代码是由哪个进程执行的：multiprocessing.current_process()
    print("main_process_id:", main_process_id, multiprocessing.current_process())

    # 2、创建子进程（自己手动创建的进程称为子进程，在__init__.py文件中已经导入的Process类）
    dance_process = multiprocessing.Process(group=None, target=dance, name="dance")
    print("dance_process:", dance_process)
    # 3、启动进程，执行对应的任务
    dance_process.start()

    sing_process = multiprocessing.Process(group=None, target=sing, name="sing")
    print("sing_process:", sing_process)
    sing_process.start()

    # 主进程执行唱歌任务
    # sing()