import pleasetransfer
import socket
import hashlib 
import sys
import time
import binascii

def crc32(string):
	string = (binascii.crc32(string)&0XFFFFFFFF)
	return "%08X" % string

t=pleasetransfer.pleasetransfer(True)
t.send_setup()
t.rec_setup()
t.settimeout(1)

input =''.join(sys.stdin)
output = open("output.txt","w")

# translate text file to binary file
length = len(input)
bin_input = ""
final_bin_input = ""
while True:
	
	for i in range(0,length):
		# convert each character into binary bits
		binary_data = bin(ord(input[i]))
		bin_len = len(binary_data)

		if(bin_len != 9):
			binary_data = binary_data+'0'
		# now you have 9 bits

		bin_input = bin_input+binary_data

	break
# now we want to remove 0b from the string

length = len(bin_input)
while True:
	try:
		new_chunk = bin_input[i+2:i+9]
		i+=9

		if new_chunk == '':
			break

		final_bin_input = final_bin_input + new_chunk
	except Exception as e:
		print e

j = 0
# i is seq number
i = 0
# creating 1024 segments
while True:
	try:
		chunk = final_bin_input[j:j+6976]
		#j+=872

		if chunk == '':
			pass
			#if i > 700:
			#	print chunk
			#	break
		else:	
			seq = bin(i)[2:].zfill(16)
			length = len(chunk)
			if length == 6976:
				data = chunk
				TCP = seq + data
				checksum = crc32(TCP)
			elif length!=6976:
				data = chunk[2:].zfill(6976)
				TCP = seq + data
				checksum = crc32(TCP)

			checksum = bin(int(checksum, 16))[2:].zfill(128)

			TCP_segment = '0b' + TCP + checksum
			print len(TCP_segment)
			#print 'seq:'+seq+'\n'
			#print 'data:'+data+'\n'
			#print 'checksum:' + checksum + '\n'

			# start sending bits
			# this is send and receive section
			t.sendbits(TCP_segment)
			#print 'TCP:' + TCP_segment
			#print len(TCP_segment)
			ack=t.recbits()
			#print 'ack:' + ack

			false = '0b1111111111111110'
			true = '0b0000000000000000'
	    	
			if ack == true:
				print 'Transmission successful'
				i = i+1
				j += 6976
				continue
			elif ack == false:
				print 'Retransmit Required'
				print i
				print j
				continue
			else:
				print
				continue
	except Exception as e:
		print e


