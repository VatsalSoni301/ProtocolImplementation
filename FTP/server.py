#2018201005 Vatsal Soni
import socket                
import os
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)          
print "Socket successfully created"

port = 48799
port1 = 54329

s.bind(('', port))       
print "socket binded to %s" %(port) 
  
s.listen(5)      
print "socket is listening"  
mapping={}  
#config file format domain+space+directory+space
with open("config.txt") as f:
		for line in f:
			mp=line.split(' ')   
			mapping[mp[0]]=mp[1]  
#mapping = {'127.0.0.1':'domain1/'}
delimeter="@@"
while True: 
  
   	c, addr = s.accept()      
   	print 'Got connection from', addr 
  	print "client ip+port",addr 
  	response = c.recv(1024000)
	print response
	a=response.index('/')
	domain=response[:a]
	path=mapping[domain]
	filepath=response[a+1:]
	finalpath=path+filepath
	content=""
	to_send=""
	if os.path.exists(finalpath):
		with open(finalpath) as f:
			for line in f:
				content+=line
		content_length=str(len(content))
		type_of_content="text"
		status_code=str(200)
		to_send=status_code+delimeter+type_of_content+delimeter+content_length+delimeter+content
		c.send("OK")
		c.recv(1024000)
		c.close()
	  	try: 
			s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
			print "Socket successfully created"
			print addr[0]
			s1.connect((str(addr[0]), port1)) 
			s1.send(to_send)
			s1.close()
		except socket.error as err: 
		    print "socket creation failed with error %s" %(err) 

	else:
		status_code=str(404)
		content_length=str(0)
		content="Resource Not Found"
		type_of_content="text"
		to_send=status_code+delimeter+type_of_content+delimeter+content_length+delimeter+content
		c.send("NotOk")
		c.close()
 
s.close()
