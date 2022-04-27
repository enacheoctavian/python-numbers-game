import socket


class Server:
    # we are connecting to the client from within the server
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('127.0.0.1', 28000))
        self.server_socket.listen(1)
        self.conn_socket, self.client_address = self.server_socket.accept()


class Client:
    # we are connecting to the server from within the client
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', 28000))
