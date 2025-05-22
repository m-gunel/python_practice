import selectors
import socket

def start_selector_server():
    sel = selectors.DefaultSelector()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12348))
    server_socket.listen()
    server_socket.setblocking(False)
    sel.register(server_socket, selectors.EVENT_READ, data=None)
    print("Selector-based server started on port 12348")

    while True:
        events = sel.select()
        for key, _ in events:
            if key.data is None:
                conn, addr = key.fileobj.accept()
                print("Accepted connection from", addr)
                conn.setblocking(False)
                sel.register(conn, selectors.EVENT_READ, data=addr)
            else:
                conn = key.fileobj
                data = conn.recv(1024)
                if data:
                    conn.sendall(data)
                else:
                    sel.unregister(conn)
                    conn.close()
