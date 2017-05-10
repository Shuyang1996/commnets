import pleasetransfer
from sys import argv, stdout, exit
from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM, timeout
from threading import Timer, current_thread
from tcp import tcp
import datetime

# t=pleasetransfer.pleasetransfer(True)#true for sender
# t.send_setup()
# t.rec_setup()
# t.settimeout(1)

# nextseqnum = 0
# sendbase = 0
# seq = []
# i = 0

# # open input file
# file_object = open("test.txt","r")
# # open output file
# output = open("output.txt","w")

# # convert the text file into binary file
# # only run this loop once
# for line in file_object:
# 	for letter in line:
# 		output.write(bin(ord(letter)))

# output.close()

# seprate the binary files into different chuncks with size 1500
# def filechunks(inputfile, chunksize=1500):
# 	with open(inputfile, "rb") as f:
	
# 			while True:
# 				chunk = f.read(chunksize)
# 				if chunk:
# 					yield chunk
# 				else:
# 					break

# below is to send what ever in there
# while True:
# 	try:
		
# 		for chunk in filechunks('output.txt'):
# 			new = [chunk,i]
# 			seq = new + seq
# 			i = i+1
			
# 		print seq[0]
# 		n = bin(int(seq[0], 2))

# 		t.sendbits(n)
# 		ack=t.recbits()
# 		print ack
# 		break

# 	except socket.timeout:
# 		pass

class Sender:
	def read(self):
		# buffer to store current data
		self.buffer = []

		# now open the file
		with open(self.filename, "rb") as f:
			# read file with each chuck size MSS which is 556
			current_chuck = f.read(tcp.MSS)
			# initialize sequence number
			seq = 0;
			# calculate expected ack number using tcp protocol
			expected_ack = seq + len(current_chuck)
			# now create each TCP segment

			# as long as this chunck is empty, we keep the loop running
			while current_chuck != ''
				previous_chunck = current_chuck
				current_chuck = f.read(tcp.MSS)

				# if reached the end of the file
				if(len(current_chuck) == 0 ):
					# do something
				else: 
					# creating TCP segment
					current_segment = tcp(seq,expected_ack,previous_chunk)
					# push this new segment into the buffer
					self.buffer.append(current_segment)

				seq += len(previous_chunk)
				expected_ack = seq + len(current_chuck)

			# collect transmission stats 
			self.byte_count += seq 
	def __init__ (self,argv):
		self.filename = argv[1]
		print self.filename

def main(argv):       
	Sender(argv)
	
main(argv)