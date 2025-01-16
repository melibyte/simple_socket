import socket
from socket import AF_INET, SOCK_STREAM

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12345)) 
    server_socket.listen(5)  
    print("Server is running, waiting for connections...")

    while True:
        try:
            client_socket, address = server_socket.accept()
            print(f"New connection: {address}")
            
            data = client_socket.recv(1024).decode()
            print(f"Received message: {data}")
            
            response = "Message received: " + data
            client_socket.send(response.encode())
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            client_socket.close()

except KeyboardInterrupt:
    print("\nServer is shutting down...")
except Exception as e:
    print(f"An error occurred on the server: {e}")
finally:
    server_socket.close()
