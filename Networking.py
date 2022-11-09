# ----------------- TCP/IP -----------------

import socket 

# Create Socket
s = socket.socket()

# bind socket to host(IP) and port
s.bind(host, port)

s.send()

s.listen()

s.recv()

s.close()