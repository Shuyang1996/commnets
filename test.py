import pleasetransfer
import socket
import struct

nextseqnum = 0
sendbase = 0
seq = []
i = 0

file_object = open("test.txt","r");
output = open("output.txt","w");

for line in file_object:
	for letter in line:
		output.write(bin(ord(letter)))

output.close()


def filechunks(inputfile, chunksize=1500):
	with open(inputfile, "rb") as f:
			while True:
				chunk = f.read(chunksize)
				if chunk:
					yield chunk
				else:
					break
    				
for chunk in filechunks('output.txt'):
	new = [chunk,i]
	seq = new + seq
	i = i+1
print seq[0]



# Sequence Number

# Event 1


# Event 2 
#if timeout


# Event 3

#ack=t.recbits()
#print ack
#	segment = tcp_header + b
#	start timer
#	s.sendto(segment, (dest_ip , 0 ))

