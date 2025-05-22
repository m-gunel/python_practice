import socket

def start_udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(b'Hello UDP Server!', ('localhost', 12347))
    data, _ = client_socket.recvfrom(1024)
    print("Received:", data.decode())
    client_socket.close()
