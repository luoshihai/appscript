from socket import *
import threading


def send_msg(client_socket):
    while True:
        send_content_socket = input('请输入回复内容：')
        if send_content_socket:
            client_socket.send(send_content_socket.encode('utf-8', '\n'))
        else:
            break
    client_socket.close()


def rec_msg(client_socket):
    while True:
        rec_socket = client_socket.recv(1024)
        if rec_socket:
            print('\n', rec_socket.decode('gbk'))
        else:
            break
    client_socket.close()


if __name__ == '__main__':
    # 创建套接字
    server_socket = socket(AF_INET, SOCK_STREAM)
    # 绑定ip
    add_socket = ('', 8080)
    server_socket.bind(add_socket)
    # 监听客户端数量
    server_socket.listen()

    # 如果有客户端的连接请求 则创建一个线程去运行
    while True:
        # 接收客户端的连接请求
        client_socket, client_address = server_socket.accept()

        # 创建线程去执行
        thread_socket_send = threading.Thread(target=send_msg, args=(client_socket,))
        thread_socket_rec = threading.Thread(target=rec_msg, args=(client_socket,))

        thread_socket_rec.setDaemon(True)
        thread_socket_send.setDaemon(True)

        thread_socket_rec.start()
        thread_socket_send.start()
