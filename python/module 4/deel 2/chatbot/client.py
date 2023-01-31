import socket

HOST = input("Enter server IP address: ")
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((HOST, PORT))
    print("Connected to server.")
    while True:
        client_input = input("You: ")
        client_socket.send(client_input.encode())
        if client_input.strip().lower() == 'stop':
            print("Exiting chat...")
            client_socket.send("stop".encode())
            client_socket.close()
            break
        server_response = client_socket.recv(1024).decode()
        print(f"Server: {server_response}")
except (ConnectionRefusedError, ConnectionError):
    print(f"Could not connect to server at {HOST}:{PORT}")
    client_socket.close()
