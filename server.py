""" Socket is a module for communication machines with him and exchange data together. """
import socket

# A socket object to listen client
socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_object.bind((socket.gethostname(), 1234))
socket_object.listen()

while True:
    client_socket, address = socket_object.accept()
    print(f'Connection from {address} has been established!')
    client_socket.send(bytes('Welcome to the server!', 'utf-8'))
