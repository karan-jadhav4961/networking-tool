import socket 					  #import socket to make connection over the network
host = '127.0.0.1'				#make server ip as local host
port = 9997					      #server only establish connection in this port

server=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)	#create UDP socket
server.bind((host,port))				                        #bind socket to ip and port

print(f"[+] UDP server listening on {host}:{port}")     #Print method to varify the running of server

while True:
	data, addr = server.recvfrom(4096)			            #data receive from client
	print(f"Data receive from {addr}:{data.decode()}") 	#printing the data and address
	response = "connection make succefull....."		      #make response to client
	server.sendto(response.encode(),addr)			          #send to the client
