import socket
import threading

def handle_client(conn, addr):
    print(f"[Threaded TCP] New connection from {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"[Threaded TCP] Received from {addr}: {data.decode()}")
        conn.sendall(data)
    conn.close()
    print(f"[Threaded TCP] Connection from {addr} closed")

def start_threaded_tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12346))
    server_socket.listen()
    print("Threaded TCP server started on port 12346")
    while True:
        conn, addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
