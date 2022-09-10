import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.bind('tcp://145.40.77.11:2000')
socket.setsockopt_string(zmq.SUBSCRIBE,'')

while(True):
    message = socket.recv_pyobj()
    print(message)
#socket.close()
