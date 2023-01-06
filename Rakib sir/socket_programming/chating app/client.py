import socket

HOST = '127.0.0.1'
PORT = 9990
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST,PORT))

while True:
    message = input("client: ")
    socket.send(message.encode('utf-8'))
    msg = socket.recv(1024).decode('utf-8')
    print("Form server: ",msg)
    if msg=="#":
        break