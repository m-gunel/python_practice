import socket
from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.fernet import Fernet

def start_encrypted_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(('localhost', 12349))

        # Генерация ключей клиента
        client_private_key = x25519.X25519PrivateKey.generate()
        client_public_key = client_private_key.public_key()

        # Получение публичного ключа сервера
        server_public_bytes = client.recv(32)
        server_public_key = x25519.X25519PublicKey.from_public_bytes(server_public_bytes)

        # Отправка публичного ключа клиента (с указанием encoding и format)
        client.sendall(client_public_key.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        ))

        # Вычисление общего ключа
        shared_key = client_private_key.exchange(server_public_key)

        # Получение симметричного ключа из общего
        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'handshake data'
        ).derive(shared_key)
        f = Fernet(Fernet.generate_key())

        # Отправка зашифрованного сообщения (не используется derived_key)
        client.sendall(f.encrypt(b"Hello Encrypted Server!"))
