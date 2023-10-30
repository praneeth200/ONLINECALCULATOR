import socket

def main():
    host = "127.0.0.1"  # The server's IP address
    port = 12345       # The server's port number

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        expression = input("Enter a mathematical expression (or 'exit' to quit): ")
        if expression.lower() == "exit":
            break

        client_socket.send(expression.encode())
        result = client_socket.recv(1024).decode()
        print("Result: " + result)

    client_socket.close()

if __name__ == "__main__":
    main()
