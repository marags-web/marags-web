

import socket
HOST = 'ids-doc' 
PORT = 2000        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    data = s.recv(1024)

while True:
   print('Received from IDS : ', repr(data))
   


