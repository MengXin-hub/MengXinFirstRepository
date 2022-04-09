# 1、引入包
import threading


def show_info(name, age):
    print("name: %s age: %d" % (name, age))


# 2、创建子进程，传参方式有两种：字典和数组
sub_thread = threading.Thread(target=show_info, args=("meng,x",), kwargs={"age": 23})


# 3、启动进程
if __name__ == "__main__":
    sub_thread.start()