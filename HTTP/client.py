#2018201005 Vatsal Soni
import socket 
import sys  

print "enter quit to exit"
while True:
	ip = raw_input("Enter url : ")
	print
	delimeter="@@"
	try: 
	    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	    print "Socket successfully created"
	except socket.error as err: 
	    print "socket creation failed with error %s" %(err) 
	  
	port = 49992
	try: 
		if ip == "quit":
			s.close()
			break
		host_ip = ip.split('/')
	except socket.gaierror: 
	  
	    print "there was an error resolving the host"
	    sys.exit() 
	  
	try:
		s.connect((host_ip[0], port)) 
		s.send(ip)
		response = s.recv(10240)
		to_print = response.split(delimeter)
		print "Status Code",":",to_print[0]
		print "Content Type",":",to_print[1]
		print "Content Length",":",to_print[2]
		print "*****Content*****"
		if len(to_print[3])==int(to_print[2]):
			print to_print[3]
		else:
			print "Data Corrupted"

	except:
		print "URL not found"


print "Thank You!!!"