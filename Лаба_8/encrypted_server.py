import socket
import threading
from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.fernet import Fernet


def handle_client(conn, addr):
    print(f"Encrypted connection from {addr}")

    # Генерация приватного/публичного ключа сервера
    server_private_key = x25519.X25519PrivateKey.generate()
    server_public_key = server_private_key.public_key()

    # Отправка публичного ключа клиенту (с указанием encoding и format)
    conn.sendall(server_public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    ))

    # Получение публичного ключа клиента
    client_public_bytes = conn.recv(32)
    client_public_key = x25519.X25519PublicKey.from_public_bytes(client_public_bytes)

    # Вычисление общего ключа
    shared_key = server_private_key.exchange(client_public_key)

    # Получение симметричного ключа из общего ключа
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'handshake data'
    ).derive(shared_key)
    f = Fernet(Fernet.generate_key())

    # Чтение зашифрованных данных от клиента
    data = conn.recv(1024)
    print(f"Received encrypted: {data}")
    conn.close()


def start_encrypted_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 12349))
        s.listen()
        print("Encrypted server started on port 12349")
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()
