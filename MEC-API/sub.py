import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.bind('tcp://demo:2000')
socket.setsockopt_string(zmq.SUBSCRIBE,'')

while(True):
    message = socket.recv_pyobj()
    print(message)
#socket.close()


