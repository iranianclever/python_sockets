""" Socket is a module for communication machines with him and exchange data together. """
import socket

# A socket object to receive data from server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

# While loop for get parted data from server
while True:
    msg = s.recv(8)  # 1024 is a capability parameter to receive data
    print(msg.decode('utf-8'))
