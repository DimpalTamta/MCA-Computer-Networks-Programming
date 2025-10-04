# date_server.py
# A simple TCP server that sends the current date & time to the client.
# Server keeps running until you type "quit" in the terminal.

import socket        # socket module is needed for networking (server ↔ client communication)
import datetime      # datetime module is used to get the current date & time
import threading     # threading allows us to run the "quit" listener in background

# ------------------------------
# 1. Define server address
# ------------------------------
HOST = "127.0.0.1"   # localhost (means this computer itself)
PORT = 9090          # port number (like a "door" for communication)
# Example: You could change to 9092 or 8080 if needed

# ------------------------------
# 2. Create a TCP socket
# ------------------------------
# AF_INET  → IPv4 addresses
# SOCK_STREAM → TCP protocol (reliable, connection-based)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow the port to be reused immediately after restart
# Example: Without this, restarting the server quickly may give "port already in use" error
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# ------------------------------
# 3. Bind the socket to host & port
# ------------------------------
# Example: (127.0.0.1, 9091) → means "listen only on this computer at port 9091"
server_socket.bind((HOST, PORT))

# ------------------------------
# 4. Start listening for clients
# ------------------------------
# Argument "1" → max number of clients waiting in queue (you can increase if needed)
server_socket.listen(1)
print(f"Server listening on {HOST}:{PORT} ...")

# ------------------------------
# 5. Control flag (running = True while server should run)
# ------------------------------
running = True

# ------------------------------
# 6. Function to listen for "quit" command from server terminal
# ------------------------------
def quit_listener():
    global running
    while True:
        cmd = input("Type 'quit' to stop the server: ")  # prompt user
        if cmd.lower() == "quit":  # if user types quit
            print("Shutting down server...")
            running = False
            server_socket.close()  # close the server socket
            break

# Run quit_listener in a separate background thread
# Example: This way, the server can keep serving clients while waiting for "quit" command
threading.Thread(target=quit_listener, daemon=True).start()

# ------------------------------
# 7. Main server loop
# ------------------------------
while running:   # keep running until "quit" is typed
    try:
        # Accept a new client connection
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")  
        # Example: ('127.0.0.1', 54321) → means client from localhost on random port 54321

        # Prepare current date & time as string
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Example: "2025-09-29 18:45:12"

        # Send date & time to client (encode = convert string → bytes)
        conn.sendall(now.encode())

        # Close this client connection (server still runs for others)
        conn.close()

    except OSError:
        # Happens when server_socket is closed (after quit)
        break

# ------------------------------
# 8. Server exits gracefully here
# ------------------------------
print("Server stopped.")