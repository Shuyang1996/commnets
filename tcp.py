import struct
import sys
from sys import stdout

class tcp:

	HEADER_SIZE = 20
    MSS = 556 # maximum segment size; the max of the data
    # HEADER_FORMAT explanation: source_port == 2 bytes, dest_port == 2 bytes, 
    # seq_no == 4 bytes, ack_no == 4 bytes, header_len == 2 bytes, FIN == 1 byte, 
    # ACK == 1 byte, checksum == 2 bytes and data
    HEADER_FORMAT = 'H H I I H b b 2s ' + str(MSS) + 's'
    PACKET_SIZE = HEADER_SIZE + MSS # should be 576

	def __init__(self, sequence_no, ack_no, data):
        
        self.sequence_no = sequence_no
        self.ACK_no = ack_no
        # header len is set to constnat
        self.ACK = 1
        self.data = data

