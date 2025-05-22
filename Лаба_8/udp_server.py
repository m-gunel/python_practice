import socket

def start_udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12347))
    print("UDP server started on port 12347")
    while True:
        data, addr = server_socket.recvfrom(1024)
        print("Received from", addr, data.decode())
        server_socket.sendto(data, addr)
