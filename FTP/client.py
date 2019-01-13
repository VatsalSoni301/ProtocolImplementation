#2018201005 Vatsal Soni
import socket 
import sys  

print "enter quit to exit"

port = 48799
port1 = 54329

while True:
	ip = raw_input("Enter url : ")
	print
	delimeter="@@"
	try: 
	    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	    print "Socket successfully created"
	except socket.error as err: 
	    print "socket creation failed with error %s" %(err)  
 
	try: 
		if ip == "quit":
			break
		host_ip = ip.split('/')
	except socket.gaierror: 
	  
	    print "there was an error resolving the host"
	    sys.exit() 
	  
	try:
		s.connect((host_ip[0], port))
		s.send(ip)
		response = s.recv(10240)
		print response
		if response=="OK":
			s1 = socket.socket()  
			s1.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
			s1.bind(('', port1))
			s1.listen(5)
			s.send("READY TO LISTEN")
			c, addr = s1.accept()
			response1 = c.recv(10240)
			to_print = response1.split(delimeter)
			print "Status Code",":",to_print[0]
			print "Content Type",":",to_print[1]
			print "Content Length",":",to_print[2]
			print "*****Content*****"
			s1.close()
			c.close()
			if len(to_print[3])==int(to_print[2]):
				print to_print[3]
			else:
				print "Data Corrupted"
		else:
			print "Resource Not Found!!!"
	except:
		print "URL not found"
	s.close()


print "Thank You!!!"