import socket
import os
import threading
import sys


# http协议的web服务器类
class HttpWebServer(object):
    def __init__(self, port):
        # 创建tcp服务端套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # setsockopt()设置端口号复用，表示意思：服务器程序退出端口号立即释放
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口号
        tcp_server_socket.bind(("", port))
        # 设置监听
        tcp_server_socket.listen(128)
        # 把tcp服务器的套接字作为web服务器对象的属性
        self.tcp_server_socket = tcp_server_socket

    # 处理客户端请求，使用静态方法
    @staticmethod
    def handle_client_request(new_socket):
        # 接受客户端的请求信息
        recv_data = new_socket.recv(4096)
        # 判断接收到的数据长度是否为0
        if len(recv_data) == 0:
            new_socket.close()
            return

        # 二进制解码
        recv_content = recv_data.decode("utf-8", "ignore")
        print("详细数据：\n" + recv_content)
        # 对数据按照空格进行分割
        request_list = recv_content.split(" ", maxsplit=2)
        # 获取请求的资源路径
        request_path = request_list[1]
        # *资源路径
        static = "D://python data//web服务器//static"
        # 判断请求的是否为根目录，如果是根目录设置返回信息
        if request_path == static:
            request_path = static + "//js//index.html"

        # 判断文件是否存在
        # 1、os.path.exits
        # os.path.exits("static/" + request_path)
        # 2、try.except
        try:
            # 打开文件读取文件数据,rb模式兼容打开图片格式
            with open(static + request_path, "rb") as file:  # 这里的file文件表示打开文件的对象
                file_data = file.read()
            # 提示：with open 关闭文件由系统完成
        except Exception as e:
            # 代码执行到此，说明没有请求该文件，返回404状态信息
            # 响应行
            response_line = "HTTP/1.1 404 NOT Found\r\n"
            # 响应头
            response_header = "Server: PWS/1.0\r\n"
            # 读取404页面数据
            with open(static + "//js//error.html", "rb") as file:
                file_data = file.read()
            # 响应体
            response_body = file_data

            #  把数据封装成http 响应报文格式的数据
            response = (response_line +
                        response_header +
                        "\r\n").encode("utf-8") + response_body

            # 发送给浏览器的响应报文数据
            new_socket.send(response)

        else:
            # 代码执行到此，说明文件存在，返回200状态信息
            # 响应行
            response_line = "HTTP/1.1 200 OK\r\n"
            # 响应头
            response_header = "Server: PWS/1.0\r\n"
            # 空行

            # 响应体
            response_body = file_data

            #  把数据封装成http 响应报文格式的数据
            response = (response_line +
                        response_header +
                        "\r\n").encode("utf-8") + response_body

            # 发送给浏览器的响应报文数据
            new_socket.send(response)

        finally:
            # 关闭服务与客户端的套接字
            new_socket.close()

    # 启动服务器的方法
    def start(self):
        # 循环等待接受客户端的连接请求
        while True:
            # 等待接受客户端的连接请求
            new_socket, ip_port = self.tcp_server_socket.accept()
            # 代码执行到此说明连接成功

            sub_thread = threading.Thread(target=self.handle_client_request, args=(new_socket,))
            # 设置成为守护主线程
            sub_thread.setDaemon(True)
            # 启动子线程执行对应的任务
            sub_thread.start()


def main():
    # 获取终端命令行参数
    params = sys.argv
    if len(params) != 2:
        print("执行的命令格式如下：python xxx.py 9000")
        return

    if not params[1].isdigit():
        print("执行的命令格式如下：python xxx.py 9000")
        return
    # 代码执行到此，说明命令行参数个数一定是两个且第二个参数是数字
    port = int(params[1])

    # 创建web服务器
    web_server = HttpWebServer(port)
    # 启动web服务器
    web_server.start()


# 判断是否为主模块的代码
if __name__ == '__main__':
    main()
