import socket
import keyboard as kb


def main():
    host = "192.168.23.1"  # Server IP address
    port = 12346  # Server port

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("Connected to the server")

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            else:
                try:
                    is_pressed, key = data.decode().split(",")
                    if is_pressed == "True":
                        kb.press(key)
                    else:
                        kb.release(key)
                except:
                    print(key)


    except KeyboardInterrupt:
        pass

    client_socket.close()


if __name__ == "__main__":
    main()
