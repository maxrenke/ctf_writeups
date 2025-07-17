import socket

def main():
    host = 'crypto.ctf.uscybergames.com'
    port = 5001

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        message = b"AAAAAAAAAAA\n"
        sock.sendall(message)
        response = sock.recv(4096)
        print(response.decode(errors='replace'))

if __name__ == '__main__':
    main()
