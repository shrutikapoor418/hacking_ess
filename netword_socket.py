import socket
sev_Add=input("type ip addess o`f sserver")
sev_port=int(input("port pls"))
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((sev_Add, sev_port))
s.listen(1)
print("server started waiting for connectio")
connection, address=s.accept()
print("client connected with address", address)
while 1:
    data=connection.recv(1024)
    if not data:
        break
    connection.sendall(b'--message recieved--\n')
    print(data.decode('utf-8'))
    connection.close()
