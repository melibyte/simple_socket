# socket_playground
A simple and concise Python example of TCP client and server communication.

## Table of Contents
1. [Socket Communication Workflow](#socket-communication-workflow)
2. [Requirements](#requirements)
3. [Usage](#usage)
4. [Code Comments](#code-comments)

## Socket Communication Workflow
#### basic_server.py
1. The server creates a socket and starts listening on a specified IP address and port.
2. It listens for incoming connections and accepts a client when one attempts to connect.
3. A message from the client is received, a response is prepared, and it is sent back to the client.
4. The connection is closed, and the server waits for the next connection.

####  basic_client.py
1. The client socket is created and attempts to connect to the specified IP address and port number.
2. If the connection is successful, a message is sent to the server.
3. The response from the server is received and printed to the screen.
4. If any error occurs, an appropriate error message is displayed.
5. Regardless of whether an error occurs, the socket connection is gracefully closed.


## Requirements
- Python 3.x

## Usage

 **1. Start the Server**  
 Open a terminal and run the following command:
 ```console
python3 server.py
```
This command starts the server and starts listening for connections. You will see a message like the following:
 ```console
Server is running, waiting for connections...
```

**2. Run the Client**
Open another terminal and run the following command:
 ```console
python3 client.py
```
This command starts the client, sends a message to the server, and receives a response from the server. You should see output like this:
 ```console
Response from the server: Message received: Hello Server !
```

## Code Comments:
- socket.socket(): Creates a TCP socket.
- socket.AF_INET: Specifies the IPv4 address family, indicating that IPv4 addresses (e.g., 127.0.0.1) will be used for communication.
- socket.SOCK_STREAM: Specifies the use of the TCP (Transmission Control Protocol) for reliable, connection-oriented communication.
- bind(): Binds the socket to a specific IP address and port.
- listen(): Allows the server to listen for incoming connections.
- accept(): Accepts a connection from a client.
- recv(): Receives data from the client.
- send(): Sends data to the client.
- encode(): Converts a string into a bytes-like object, as the send() method requires data to be transmitted in the form of bytes.
- connect(): Allows the client to connect to the server.




