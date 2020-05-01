import socket as s
hostname = s.gethostname()
IP = s.gethostbyname(hostname)
print (IP)
