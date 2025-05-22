import socket

def start_tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    client_socket.sendall(b'Hello TCP Server!')
    data = client_socket.recv(1024)
    print("Received:", data.decode())
    client_socket.close()
