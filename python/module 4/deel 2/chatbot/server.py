import socket

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server started at {HOST}:{PORT}")
while True:
    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} has been established.")
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(f"Received message from client: {data}")
            if data == 'stop':
                client_socket.send("Exiting chat...".encode())
                client_socket.close()
                break
            server_input = input("Server: ")
            client_socket.send(server_input.encode())
        except (ConnectionResetError, BrokenPipeError):
            print(f"Connection with {client_address} closed.")
            client_socket.close()
            break
