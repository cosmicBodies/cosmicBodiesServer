import socket
import json

from fakeEnv import host,port

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind((host,port))
server_socket.listen(1)
print("Waiting for connection")


class Server():
    def __init__(self):
        server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_socket.bind((host,port))
        server_socket.listen(1)
        print('Waiting for connection')
        server_socket.recv(1024).decode()
        print("User accepted")