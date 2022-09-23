import socket
#HOST = socket.gethostbyname('ids_dns4')# Standard loopback interface address (localhost)
#PORT = 9898        # Port to listen on (non-privileged ports are > 1023)
HOST = 'ids5'
PORT = 2000 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #s.connect((HOST,PORT))
    s.bind((HOST,PORT))
    s.listen()
    conn, addr = s.accept()

#   with conn:
        #print('Connected by', addr)

    while True:
        data = (b'attack')
        #if not data:
        #   break
        conn.sendall(data)

