import socket
import keyboard as kb
import time

special_keys = {
    'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j',
    'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't',
    'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z', '!': '1', '@': '2', '#': '3', '$': '4',
    '%': '5', '^': '6', '&': '7', '*': '8', '(': '9', ')': '0', '~': '`', '_': '-', '+': '=', '{': '[',
    '}': ']', '|': '\\', ':': ';', '"': "'", '<': ',', '>': '.', '?': '/'
}

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
                is_pressed, key = data.decode().split(",")
                if is_pressed == "True":
                    if key in special_keys:
                        kb.press(special_keys[key])
                    else:
                        kb.press(key)

                else:
                    if key in special_keys:
                        kb.release(special_keys[key])
                    else:
                        kb.release(key)
            time.sleep(0.01)


    except KeyboardInterrupt:
        pass

    client_socket.close()


if __name__ == "__main__":
    main()
