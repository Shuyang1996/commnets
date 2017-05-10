import pleasetransfer
import socket
import hashlib 
import sys
import time
import binascii

def crc32(string):
	string = (binascii.crc32(string)&0XFFFFFFFF)
	return "%08X"%string

t=pleasetransfer.pleasetransfer(True)
t.send_setup()
t.rec_setup()
t.settimeout(1)

input=''.join(sys.stdin)
output = len(input)

length = len(input)
bin_input = ""
final_bin_input = ""
# while True:
# 	for i in range(0,length):
# 		binary_data = bin(ord(input[i]))
# 		bin_len = len(binary_data)

# 	    if(bin_len != 9):
# 	    	binary_data = binary_data + '0'

# 	    bin_input = bin_input + binary_data
# 	break

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