import socket
import random

def main():
    # Create a socket object to accept incoming connections
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Bind the socket to a port
        sock.bind(("localhost", 8080))

        # Listen for incoming connections
        sock.listen(5)
        print("Listening on port 8080...")

        while True:
            # Accept an incoming connection
            client_sock, client_addr = sock.accept()
            with client_sock:
                print(f"Received connection from {client_addr}")

                # Randomly choose the server port, either 8000 or 8001
                server_port = random.choice([8000, 8001])

                # Create a socket object to connect to the chosen server
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
                    server_sock.connect(("localhost", server_port))
                    print(f"Forwarding connection to localhost:{server_port}")

                    # Forward the connection: receive data from client and send to server
                    data = client_sock.recv(1024)
                    if data:
                        server_sock.sendall(data)

                    # Optionally, you can also return the response from the server to the client:
                    # response = server_sock.recv(1024)
                    # client_sock.sendall(response)

if __name__ == "__main__":
    main()
