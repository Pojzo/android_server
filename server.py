from config import MAX_CLIENTS

import socket
import threading

HOST = '192.168.100.7'
PORT = 12345

# create a TCP server socket that listens on port 44444 

class TCPServer:
    def __init__(self, port: int, mode="normal", host: str = 'localhost'): 
        self.host = host
        self.port = port
        self.num_clients = 0
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        # create a thread to listen for incoming connections

    def listen(self) -> None:
        self.socket.listen(MAX_CLIENTS)
        while True:
            while self.num_clients >= MAX_CLIENTS:
                pass

            client, address = self.socket.accept()
            self.num_clients += 1
            client.settimeout(60)
            threading.Thread(target=self.listen_to_client, args=(client, str(address))).start()
    
    def listen_to_client(self, client: socket, addr: str) -> None:
        print(f"Client {addr} connected")
        # the server always starts by saying "HELLO"
        client.sendall("HELLO\n".encode())
        while True:
            try:
                data = client.recv(1024).decode()
            except ConnectionResetError:
                print("Connection reset by the client")
                break
            if data == "BYE":
                break
            
            input_data = input(f"Client {addr} sent: {data}. Enter a response: ")
            input_data += "\n"

            try:
                client.sendall(input_data.encode())
            except ConnectionResetError:
                break

        self.num_clients -= 1
        print("Client disconnected")
        print("--------------------")



server = TCPServer(PORT)
server.listen()