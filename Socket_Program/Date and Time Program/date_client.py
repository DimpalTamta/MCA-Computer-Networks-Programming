# date_client.py
# A simple TCP client that receives date & time from the server

import socket

HOST = "127.0.0.1"   # server address
PORT = 9090

# 1. create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. connect to server
client_socket.connect((HOST, PORT))

# 3. receive data
data = client_socket.recv(1024).decode()

print(f"Server date & time : {data}")

# 4. close socket
client_socket.close()