import socket
import threading


# 处理客户端请求的任务
def handle_client_request(ip_port, new_client):
    print("客户端的ip和端口号为：", ip_port)
    # 每次客户端和服务器建立连接成功都会返回一个新的套接字
    # tcp_server_socket只负责接受客户端的连接请求

    while True:
        # 5、接受数据
        recv_data = new_client.recv(1024)

        if recv_data:
            print("接收的数据长度是：", len(recv_data))
            recv_content = recv_data.decode("gbk")

            print("接收客户端的数据为：", recv_content, ip_port)
            send_content = "问题正在处理中···"
            # 收发消息都使用返回的这个新的套接字

            send_data = send_content.encode("gbk")
            # 6、发送数据到客户端
            new_client.send(send_data)

        else:
            # 客户端关闭连接
            print("客户端下线了：", ip_port)
            break

    # 关闭服务与客户端套接字，表示和客户端终止通信
    new_client.close()


if __name__ == '__main__':

    # 1、创建服务器套接字对象
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # setsockopt()设置端口号复用，表示意思：服务器程序退出端口号立即释放
    # SOL_SOCKET：表示当前套接字
    # SO_REUSEADDR：表示端口号的选择
    # True： 确定是复用

    # 2、绑定端口号
    tcp_server_socket.bind(("", 8080))
    # 第一个参数表示ip地址，一般不指定
    # 第二个参数表示端口号

    # 3、设置监听
    tcp_server_socket.listen(128)
    # 128：表示最大等待建立连接的个数

    while True:  # 服务端服务多个客户端

        # 4、等待接受客户端的连接请求
        new_client, ip_port = tcp_server_socket.accept()
        # 代码执行到此说明客户端与服务端连接成功，创建子线程
        sub_thread = threading.Thread(target=handle_client_request, args=(ip_port, new_client))
        # 设置守护主线程，主线程退出子线程直接销毁
        sub_thread.setDaemon(True)
        # 启动子线程执行对应的任务
        sub_thread.start()

    # 7、关闭套接字
    # tcp_server_socket.close()  # 这段代码可去掉，因为服务端的程序需要一直运行





