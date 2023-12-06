import socket
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1239))
s.listen(1)
def f(*args):
    print(args)
    args.send(f"neponel".encode("utf-8"))

while True:
    clientsocket, address = s.accept()
    threading.Thread(target=f(), args=(clientsocket,)).start()
    clientsocket.send(f"got it?".encode("utf-8"))
    clientsocket.close()
    