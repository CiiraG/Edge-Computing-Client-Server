import socket

HOST = '127.0.0.1'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()

print("Server is running...")
print("Waiting for client...")

conn, addr = server.accept()

print("Connected by:", addr)

while True:
    data = conn.recv(1024).decode()

    if not data:
        break

    print("Client:", data)

    response = "Server received: " + data

    conn.send(response.encode())

conn.close()
server.close()
