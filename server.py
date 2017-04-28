from socket import *
import sys
from threading import Thread
from http.server import BaseHTTPRequestHandler, HTTPServer

if sys.argv[1:]:
	serverport = int(sys.argv[1])
else:
	serverport = 8080

serversocket = socket(AF_INET,SOCK_STREAM)#creating a socket with ipv4 address and TCP connection
serversocket.bind(('',serverport))#binding host ip with port no.
serversocket.listen(5)#server can maintain a backlog of 5 connxns
print("\nStarting Server on port " +str(serverport))

class newThread(Thread):
	def __init__(self,id):
		Thread.__init__(self)
		self.id = id

	
	def run(self):
		print ("Thread id is :" +str(self.id))
		print ("Connected with "+addr[0])
		req = connxnsock.recv(1024)
		req = req.decode('utf-8')#decodes the received encoded request
		filename = req.split()[1].partition('/')[2]#gets the filename from the http request msg
		try:#when the requested file exists
			fopen = open(filename,'r')
			fcontent	= fopen.readlines()
			fopen.close()	
			resp = """\
HTTP/1.1 200 OK
			
File Exists!
			"""
			connxnsock.send(resp.encode('utf-8'))
			for i in range(0,len(fcontent)):
				connxnsock.send(fcontent[i].encode('utf-8'))
			connxnsock.close()
		except IOError:#when the requested file doesn't exist
			resp = """\
HTTP/1.1 404 Not Found
			"""
			connxnsock.send(resp.encode('utf-8'))#encoded as only byte format can be sent
			connxnsock.close()
				

threads = []#keeps track of all threads
i = 1#thread id
while(1):
	connxnsock, addr = serversocket.accept()
	details = []
	details = (str(connxnsock)).split(',')
	print("\nHost:" +addr[0] +"; socket"+ details[1] +"; socket"+ details[2]+"; " +details[3])	
	t = newThread(i)#thread created with a new id that is passed as argument
	threads.append(t)
	t.start()#the start function in turn calls the run function in newThread class
	i += 1