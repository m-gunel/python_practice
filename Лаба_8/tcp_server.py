import socket

def start_tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("TCP server started on port 12345")

    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("Received:", data.decode())
        conn.sendall(data)
    conn.close()
    server_socket.close()
