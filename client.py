from socket import *
import sys, time

#following if-else statements are for command line arguments passed
if sys.argv[1:]:
	servername = str(sys.argv[1])
else:
	servername = "10.226.11.75"

if sys.argv[2:]:
	serverport = int(sys.argv[2])
else:
	serverport = 8080

if sys.argv[3:]:
	filename = str(sys.argv[3])
else:
	filename = "socket.txt"

clientsocket = socket(AF_INET, SOCK_STREAM)#creating a socket with ipv4 address and TCP connection
clientsocket.connect((servername,serverport))#connects server ip address with server port no.
print("Starting Client...")
print("host name of server: "+str(servername))

req = """\
GET /"""+filename+""" HTTP/1.1
Host: localhost:8080
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari
/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding: gzip, deflate, sdch
Accept-Language: en-US,en;q=0.8
"""

req = req.encode('utf-8')
send_time = time.time()
clientsocket.send(req)
resp = clientsocket.recv(1024)
recv_time = time.time()
rtt = round(recv_time - send_time, 3)#calculating round trip time
print (resp.decode('utf-8'))
print("Round Trip Time in seconds: "+ str(rtt))

for i in range(1,10):#receiving and printing file on client side 
	file = clientsocket.recv(2048)
	print (file.decode('utf-8'))
clientsocket.close()