import socket
import tkinter as tk


HOST = '127.0.0.1'
PORT = 12345


def send_message():
    message = client_text.get()
    client_socket.send(message.encode())
    if message == 'stop':
        client_socket.close()
        root.quit()
    client_text.set("")
    receive_message()


def receive_message():
    try:
        data = client_socket.recv(1024).decode()
        server_text.set(data)
    except:
        pass

    root.after(10, receive_message)


root = tk.Tk()
root.title("Chat Client")
root.geometry("300x400")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

client_text = tk.StringVar()
server_text = tk.StringVar()

client_label = tk.Label(root, text="Client")
client_label.pack()

client_entry = tk.Entry(root, textvariable=client_text)
client_entry.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

server_label = tk.Label(root, textvariable=server_text)
server_label.pack()

root.after(10, receive_message)
root.mainloop()
