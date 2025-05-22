import socket
import threading
import time

def client_task(id):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(('localhost', 12346))
        message = f"Hello from client {id}"
        print(f"[Client {id}] Sending: {message}")
        sock.sendall(message.encode())
        response = sock.recv(1024).decode()
        print(f"[Client {id}] Received: {response}")
        time.sleep(1) 

# Запускаем 3 клиента одновременно
for i in range(3):
    threading.Thread(target=client_task, args=(i,), daemon=True).start()

time.sleep(3)  # Ждём, чтобы все клиенты успели завершиться
