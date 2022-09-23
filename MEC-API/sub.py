#import zmq

#context = zmq.Context()
#socket = context.socket(zmq.SUB)
#socket.bind('tcp://mecapi-demo:8080') for IDS client 
#socket.setsockopt_string(zmq.SUBSCRIBE,'')

#while(True):
#   message = socket.recv_pyobj()
#   print(message)
#socket.close()

import socket
HOST = 'ids-demo.MyApp' 
PORT = 2000        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    data = s.recv(1024)

while True:
    print('Received', repr(data))


