import socket
import keyboard
import time

def main():
    host = "127.0.0.1"  # Server IP address
    port = 12346       # Server port

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("Connected to the server")

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            else:
                key = data.decode()
                print(key)
                keyboard.press_and_release(key)
    except KeyboardInterrupt:
        pass

    client_socket.close()

if __name__ == "__main__":
    main()
