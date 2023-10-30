import socket

def calculate(expression):
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Error: Invalid expression"

def main():
    host = "127.0.0.1"  # The server's IP address
    port = 12345       # The server's port number

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Calculator server is listening on {}:{}".format(host, port))

    while True:
        client_socket, addr = server_socket.accept()
        print("Connection from: {}".format(addr))
        
        data = client_socket.recv(1024).decode()
        print("Received: " + data)
        
        result = calculate(data)
        client_socket.send(result.encode())

        client_socket.close()

if __name__ == "__main__":
    main()
