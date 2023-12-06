import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1241))
server_send = s.recv(1024).decode('UTF-8')
print(server_send)
client_answer = input() #hello
s.send(client_answer.encode("UTF-8"))

# server_send = s.recv(1024).decode('UTF-8')
# print(server_send)
# client_answer = input()
while True:
    server_send = s.recv(2048).decode('UTF-8')
    print(server_send)
    if server_send == "Game Over!":
        s.close()
        break
    if server_send[0] != "Y":
        client_answer = input()
        s.send(client_answer.encode("UTF-8"))
