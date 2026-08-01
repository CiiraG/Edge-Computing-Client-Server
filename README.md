# Edge-Computing-Client-Server Application

## Student Details

**Name:** Praise Ciira  
**Course:** Bachelor of Science in Computer Science  
**Unit:** Distributed Systems

---

## Project Description

This project demonstrates a simple client-server application using Python socket programming. The application enables a client process to communicate with a server process over TCP sockets on localhost (127.0.0.1).

---

## Objectives

- Implement a simple client-server application.
- Demonstrate Inter-Process Communication (IPC) using TCP sockets.
- Verify successful message exchange between the client and server.

---

## Technologies Used

- Python 3
- Socket Library
- Visual Studio Code
- Git & GitHub

---

## Project Structure

```
Edge-Computing-Client-Server/
│── client.py
│── server.py
│── README.md
└── screenshots/
```

---

## How to Run

1. Open the project in Visual Studio Code.
2. Open a terminal and run:

```bash
python server.py
```

3. Open a second terminal and run:

```bash
python client.py
```

4. Enter a message when prompted.
5. The server receives the message and sends a response back to the client.

---

## Sample Output

### Server

```
Server started...
Waiting for client connection...
Connected by ('127.0.0.1', 54321)
Received: Hello Server
```

### Client

```
Enter your message:
Hello Server

Server Reply:
Message received successfully: Hello Server
```

---

## IPC Technique Used

This project uses **TCP sockets**, an Inter-Process Communication (IPC) mechanism that enables communication between a client and server over a network.

---

## Conclusion

The application successfully demonstrates communication between a client and server using TCP sockets. Messages are exchanged reliably, confirming successful IPC implementation.

## Screenshots

Screenshots demonstrating successful communication are available in the `screenshots` folder.