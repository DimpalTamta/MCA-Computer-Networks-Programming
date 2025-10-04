# echo_server.py
# A simple TCP Echo Server.
# It listens for clients, receives data, and sends the SAME data back to the client.
# The server keeps running until you type "quit" in the terminal.

import socket      # socket module → required for networking
import threading   # threading → to run "quit" command listener in background

# ------------------------------
# 1. Define server address
# ------------------------------
HOST = "127.0.0.1"   # localhost → means run only on this computer
PORT = 9091          # port number (like a door where clients connect)

# ------------------------------
# 2. Create a TCP socket
# ------------------------------
# AF_INET = IPv4, SOCK_STREAM = TCP (reliable, connection-oriented protocol)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow reusing the port immediately after restart (avoids "port already in use" error)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# ------------------------------
# 3. Bind the socket to (HOST, PORT)
# ------------------------------
# Example: If HOST="127.0.0.1" and PORT=9091, server listens on localhost:9091
server_socket.bind((HOST, PORT))

# ------------------------------
# 4. Start listening for clients
# ------------------------------
# listen() → server waits for incoming connections
# Argument = number of connections allowed to wait in queue (use 5 or more in real apps)
server_socket.listen(5)
print(f"Echo Server listening on {HOST}:{PORT}")

# ------------------------------
# 5. Control flag (to stop server when needed)
# ------------------------------
running = True

# ------------------------------
# 6. Function to check for "quit" command from terminal
# ------------------------------
def quit_listener():
    global running
    while True:
        cmd = input()   # wait for user to type something
        if cmd.lower() == "quit":  # if user types quit
            print("Shutting down Echo Server...")
            running = False
            server_socket.close()   # stop accepting new connections
            break

# Run quit listener in background (daemon thread → ends when main program ends)
threading.Thread(target=quit_listener, daemon=True).start()

# ------------------------------
# 7. Main server loop
# ------------------------------
while running:
    try:
        # Accept a new client connection
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")
        # Example: ('127.0.0.1', 56789) → client connected from localhost on random port

        # ------------------------------
        # Inner loop → handle communication with ONE client
        # ------------------------------
        while True:
            # Receive up to 1024 bytes of data
            data = conn.recv(1024)
            # Example: if client sends "Hello", then data = b"Hello"

            if not data:
                # If client sends nothing → connection closed
                print(f"Connection closed by {addr}")
                break

            # Send the SAME data back to client (Echo!)
            conn.sendall(data)
            # Example: Client sends "Hi" → Server sends "Hi" back

        # Close this client connection (server still runs for other clients)
        conn.close()

    except OSError:
        # This happens when server_socket is closed after "quit"
        break

# ------------------------------
# 8. Server exits gracefully
# ------------------------------
print("Echo Server stopped.")
