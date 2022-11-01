import socket
from timeit import repeat

c = ('localhost' , 12345)

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

client.connect(c)

data = client.recv(1024)
print(data.decode())


