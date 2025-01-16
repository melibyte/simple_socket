import socket
from socket import AF_INET, SOCK_STREAM

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12345))
    print("Successfully connected to the server.")
    
    message = "Hello, server!"
    client_socket.send(message.encode())
    print(f"Message sent to the server: {message}")
    
    response = client_socket.recv(1024).decode()
    print(f"Response from the server: {response}")

except ConnectionRefusedError:
    print("Connection failed. Is the server running?")
except ConnectionResetError:
    print("Connection was reset by the server.")
except socket.error as e:
    print(f"A socket error occurred: {e}")
finally:
    client_socket.close()
    print("Connection closed.")

