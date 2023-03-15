from config import *
import socket

HOST = '127.0.0.1'
PORT = 44444

# create a TCP server socket that listens on port 44444 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.rect(1024)
            if not data:
                break

            conn.sendall(data)