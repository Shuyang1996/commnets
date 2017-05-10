import pleasetransfer
import socket
import hashlib 
t=pleasetransfer.pleasetransfer(True)
t.send_setup()
t.rec_setup()
t.settimeout(1)

#file_object = open("file_1.txt","r");
#output = open("output.txt","w");

#for line in file_object:
#	for letter in line:
#		output.write(bin(ord(letter)))

#output.close()
def filechunks(inputfile, chunksize=9):
	with open(inputfile, "rb") as f:
    		while True:
        		chunk = f.read(chunksize)
        		if chunk:
        			yield chunk
    			else:
    				break


def is_corrupted(instance):
    return (instance.checksum == TCP_segment.checksum_function(instance))

i=0
while True:
	try:
		for chunk in filechunks('output.txt'):
			print 'chunk:' + chunk
			seq = bin(i)[2:].zfill(16)
			data = chunk[2:len(chunk)]
			TCP = seq + data
			checksum = (hashlib.md5(TCP).hexdigest())
			checksum = bin(int(checksum, 16))[2:].zfill(128)
			TCP_segment = TCP + checksum
			print 'seq:'+seq+'\n'
			print 'data:'+data+'\n'
    		print 'checksum:' + checksum + '\n'
    		t.sendbits(TCP_segment)
    		print 'TCP:' + TCP_segment
    		print len(TCP_segment)
    		ack=t.recbits()
    		#ack=ack[]
        	#print 'ack:' + ack
        	if ack!=seq:
        		print('Ack was no good')
        		# Retransmit
        		t.sendbits(TCP_segment)
        	else:
        		pass
			i = i+1
       	except socket.timeout:
       		pass
    	break
