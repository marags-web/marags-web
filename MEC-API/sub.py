import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.bind('tcp://$IPAddr:$Port')
socket.setsockopt_string(zmq.SUBSCRIBE,'')

while(True):
    message = socket.recv_pyobj()
    print(message)
#socket.close()


