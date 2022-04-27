from Utility.utility import getrandomnumber, compare, validator
from client_server import Server

server = Server()
print("Server has started")
# First we receive the user input
guess = server.conn_socket.recv(512).decode()


if not isinstance(int(guess), int) and 0 < int(guess) < 101:
    print('Game over, next time use only numbers ranging from 1 to 100')
    exit(0)
# generate a int within our desired range
mynumber = getrandomnumber()

if validator(int(guess)) != 1:
    server.conn_socket.send("lost".encode())
if compare(mynumber, int(guess)) == 1:
    server.conn_socket.send("won".encode())
if compare(mynumber, int(guess)) == 0:
    server.conn_socket.send("greater".encode())
if compare(mynumber, int(guess)) == 2:
    server.conn_socket.send("lesser".encode())

while True:
    guess=server.conn_socket.recv(512).decode()
    if validator(int(guess)) == 0:
        server.conn_socket.send("lost".encode())
        break
    if compare(mynumber, int(guess)) == 1:
        server.conn_socket.send("won".encode())
        break
    if compare(mynumber, int(guess)) == 0:
        server.conn_socket.send("greater".encode())
    if compare(mynumber, int(guess)) == 2:
        server.conn_socket.send("lesser".encode())
