import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 5001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))

print("UDP Server started !")
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message:", data.decode('utf8'), " from ", addr)
    sock.sendto(data, addr)
