from tcp_server import start_tcp_server
from tcp_client import start_tcp_client
from threaded_tcp_server import start_threaded_tcp_server
from udp_server import start_udp_server
from udp_client import start_udp_client
from selector_server import start_selector_server
from encrypted_server import start_encrypted_server
from encrypted_client import start_encrypted_client
import threading, time

if __name__ == "__main__":
    threading.Thread(target=start_tcp_server, daemon=True).start()
    time.sleep(0.5)
    start_tcp_client()

    threading.Thread(target=start_threaded_tcp_server, daemon=True).start()
    time.sleep(0.5)

    threading.Thread(target=start_udp_server, daemon=True).start()
    time.sleep(0.5)
    start_udp_client()

    threading.Thread(target=start_selector_server, daemon=True).start()
    time.sleep(0.5)

    threading.Thread(target=start_encrypted_server, daemon=True).start()
    time.sleep(0.5)
    start_encrypted_client()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Server shutting down.")

