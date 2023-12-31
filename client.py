""" Socket is a module for communication machines with him and exchange data together. """
import socket

# A socket object to receive data from ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

full_msg = ''
# While loop for get parted data from server
while True:
    msg = s.recv(8)  # 1024 is a capability parameter to receive data
    if len(msg) <= 0:
        break
    full_msg += msg.decode('utf-8')

print(full_msg)
