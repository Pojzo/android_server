from config import *
import socket

HOST = '192.168.100.7'
PORT = 12345

# create a TCP server socket that listens on port 44444 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server is listening on port 12345")
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if data == "BYE":
                break
            
            print(data.decode())
            conn.sendall(data)