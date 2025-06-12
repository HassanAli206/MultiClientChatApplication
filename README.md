Chatroom Application

Overview
This is a multi-user chatroom application implemented in Python, supporting both TCP and UDP protocols. It allows multiple clients to connect to a server, send messages, and receive real-time broadcasts of messages from other clients. The application includes both command-line (CLI) and graphical user interface (GUI) clients, built using Tkinter, and supports concurrent client handling using threading.

Features
TCP and UDP Support: Choose between reliable TCP or lightweight UDP communication protocols.
CLI and GUI Interfaces: Interact via command-line or a user-friendly Tkinter GUI.
Real-Time Messaging: Messages are broadcast to all connected clients instantly.
Client Management: Ensures unique client names and handles join/leave events.
Graceful Shutdown: Servers notify clients on shutdown, and clients can exit cleanly.
Customizable: Run servers and clients with a specified port (default: 12345) and client name via command-line arguments.

Requirements
Python 3.x
Tkinter (for GUI clients, included with standard Python installation)
No external dependencies required

Installation
1. Clone or download the repository to your local machine.
2. Ensure Python 3.x is installed on your system.
3. No additional setup is required as Tkinter is included with Python.

Usage
Running the Server
TCP Server:
    python tcp_server.py
 
UDP Server:
  python udp_server.py

Both servers run on port 12345 by default and can be stopped with `Ctrl+C`.

Running the Client
TCP CLI Client:
  python chatroom.py --name <your_name>
UDP CLI Client:
   python chatroom.py --name <your_name>

TCP GUI Client:
  python tcp_gui.py --name <your_name>
 
UDP GUI Client:
  python udp_gui.py --name <your_name>

Replace `<your_name>` with a unique username. The client connects to the server running on the same machine (localhost) at port 12345.

Example
1. Start the TCP server in one terminal:
   python tcp_server.py


2. Start multiple TCP GUI clients in separate terminals:
   python tcp_gui.py --name Alice
   python tcp_gui.py --name Bob


3. Type messages in the GUI entry field and click "Send" to broadcast. Type `exit` or close the window to leave the chatroom.

How It Works
Servers:
TCP Server: Listens for client connections, maintains a dictionary of connected clients, and broadcasts messages using TCP sockets. Each client runs in a separate thread for concurrent handling.
UDP Server: Receives and broadcasts datagrams, tracking clients by their addresses and names. No persistent connections are maintained.
Clients:
  Connect to the server with a unique name, send messages, and receive broadcasts in real-time.
  CLI clients display messages in the terminal, while GUI clients show messages in a scrollable text area (sent messages in blue, right-aligned; received messages in black, left-aligned).
  Use threading to handle sending and receiving messages concurrently.
Shutdown: Servers notify clients on shutdown, and clients handle `exit` commands or window closure gracefully.

Notes:
Ensure the server (TCP or UDP) is running before starting clients.
Use unique names for each client to avoid "Name already taken" errors.
The application assumes the server and clients run on the same machine (localhost). For remote access, modify the server address in client code.
UDP may drop messages under high network load due to its connectionless nature, while TCP ensures reliable delivery.

Troubleshooting:
Connection Errors: Ensure the server is running and the port (12345) is not blocked by a firewall.
Name Taken: Choose a unique name for each client.
No Messages Received: Verify the server is running and clients are connected to the correct protocol (TCP/UDP) and port.

License
This project is open-source. Can be used and modified for educational purpose.

