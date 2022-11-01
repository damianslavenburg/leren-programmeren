import socket 

s =  ('localhost' , 12345)

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

server.bind(s)

server.listen(2)

con , addr = server.accept()


Send_data = input(">> ")
con.sendall(Send_data.encode())

