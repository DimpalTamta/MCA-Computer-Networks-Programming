import socket

HOST = "127.0.0.1"
PORT = 9091

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    msg = input("Enter message (or 'quit' to exit): ")
    if msg == "quit":
        break
    client_socket.sendall(msg.encode())
    reply = client_socket.recv(1024).decode()
    print("Server echoed:", reply)

client_socket.close()
