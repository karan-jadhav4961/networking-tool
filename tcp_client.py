''' 
This is a simple TCP client script in Python that connects to a server running on 127.0.0.1 (localhost) at port 9998. That send some data 
to the sever and receiv data from the server and print it.
'''

import socket

target_host = "127.0.0.1"  # Server's IP address
target_port = 9998         # Must match the server's port


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # Create an IPv4 TCP socket
client.connect((target_host, target_port))                    # This is 3-way handshaking, by the way client send SYN, server reply
                                                              # SYN+ACK, and again client sent ACK
client.send(b"Hello, Server! hii brother dfjkglgjldj")        # Send data to server in byte to unserstand every machines
response = client.recv(4096)                                  # Receive the server's response
print(f"Server response: {response.decode('utf-8')}")         # Print the server response
client.close()                                                # Close the connection
