import socket                                           #import socket to make communication possible over the network
target_host="127.0.0.1"                                 #target host that is nothing but loopback ip
target_port=9997                                        #target port 

client=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     #create object of the socket
client.sendto(b"ASDFDSASDFDS",(target_host, target_port))   #send data to the target in byte formate, with attach the ip and port of the target
data, addr = client.recvfrom(4096)                          #Receive data and ip&port from the target which the size should be less than or equal to 4096 
print(data.decode())                                        #print data, which receive from target
print(addr)                                                 #print the addres and port of the target
client.close()                                              #close the udp socket
