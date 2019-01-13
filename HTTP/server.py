#2018201005 Vatsal Soni
import socket                
import os
s = socket.socket()          
print "Socket successfully created"

port = 49992            
  
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
	response = c.recv(10240)
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
	else:
		status_code=str(404)
		content_length=str(0)
		content="Resource Not Found"
		type_of_content="text"
		to_send=status_code+delimeter+type_of_content+delimeter+content_length+delimeter+content

	c.send(to_send) 
	c.close()
