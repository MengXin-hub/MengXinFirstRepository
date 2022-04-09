# 导入套接字socket包
import socket

if __name__ == '__main__':
    # 1、创建tcp客户端套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # AF_INE：ipv4地址类型
    # SOCK_STREAM：tcp传输协议类型

    # 2、和服务端套接字建立连接
    tcp_client_socket.connect(("10.10.10.171", 8080))

    # 3、发送数据到服务器
    send_content = "你好！这是巴塞罗那足球俱乐部"  # input()
    send_data = send_content.encode("gbk")
    tcp_client_socket.send(send_data)
    # encode对字符串进程编码成为二进制数据
    # Windows里面的网络调试助手使用gbk编码
    # Linux里面的网络调试助手使用utf-8编码（国际标准）

    # 4、接受服务器的数据
    recv_data = tcp_client_socket.recv(1024)
    recv_content = recv_data.decode("gbk")
    print("接受服务端的数据为：", recv_content)
    # 1024：表示每次接收到的最大字节数
    # decode对二进制数据进行解码

    # 5、关闭套接字
    tcp_client_socket.close()



