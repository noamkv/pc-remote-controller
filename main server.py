import keyboard as kb
import socket
from pynput.keyboard import Listener


def on_key_event(client_socket):
    def callback(e):
        if e.event_type == kb.KEY_DOWN:
            key_event = f"Key {e.name} was pressed"
            print(key_event)
            client_socket.send(("True," + e.name).encode())

        elif e.event_type == kb.KEY_UP:
            key_event = f"Key {e.name} was released"
            print(key_event)
            client_socket.send(("False," + e.name).encode())
    return callback



def main():
    # Set up the server
    host = "0.0.0.0"  # Server IP address
    port = 12346  # Port to listen on

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    kb.hook(on_key_event(client_socket))

    try:
        while True:
            pass  # Keep the program running
    except KeyboardInterrupt:
        pass

    server_socket.close()


if __name__ == "__main__":
    main()A
