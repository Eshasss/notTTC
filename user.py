import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1240))
server_send = s.recv(1024).decode('UTF-8')
print(server_send)
client_answer = input() #hello
s.send(client_answer.encode("UTF-8"))

server_send = s.recv(1024).decode('UTF-8')
print(server_send)

while True:
    client_answer = input()
    s.send(client_answer.encode("UTF-8"))
    c = s.recv(2048).decode('UTF-8')
    if c == "Game Over!":
        print(c)
        break
    print(c)
    