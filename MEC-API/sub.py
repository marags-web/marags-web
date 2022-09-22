#import zmq

#context = zmq.Context()
#socket = context.socket(zmq.SUB)
#socket.bind('tcp://demo:2000')
#socket.setsockopt_string(zmq.SUBSCRIBE,'')

#while(True):
#   message = socket.recv_pyobj()
#   print(message)
#socket.close()

import socket
HOST = socket.gethostbyname('ids_dns4')# Standard loopback interface address (localhost)
PORT = 9898        # Port to listen on (non-privileged ports are > 1023)
#socket.bind('tcp://demo:2000')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)

while True:
    print('Received', repr(data))


