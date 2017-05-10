import pleasetransfer
import hashlib 
import binascii

output = open("output.txt","w");

def bits2string(b=None):
    a =''
    while b != "":
         a = a + chr(int(b[0:8], 2))
         b = b[8:]
    return a


def crc32(string):
    string = (binascii.crc32(string)&0XFFFFFFFF)
    return "%08X" % string

t=pleasetransfer.pleasetransfer(False)#False for receiver
t.rec_setup()
t.send_setup()
sequence = 0
# t.settimeout(10)
while True:
    rcv = t.recbits()
    length = len(rcv)

    print 'rcv:' + rcv + '\n'

    if length == 7120:
        seqnumber = rcv[0:18]
        data = rcv[18:6994]
        checksum = rcv[6994:]
#        print 'CHECKSUM: '+checksum
        seqnumber1 = seqnumber[2:18]

        new_checksum = crc32(seqnumber1+data)
        # new_checksum = (hashlib.md5(seqnumber1+data).hexdigest())
        new_checksum = bin(int(new_checksum, 16))[2:].zfill(128)
        print 'new checksum: '+ new_checksum + '\n'

    # if this is the last package and size does not match, we do something else
    elif length!= 7120:

        print len(rcv)
        print 'HERE'+rcv
        # get the checksum start from the end of the data file
        checksum = rcv[len(rcv)-128:]
        print 'CHECKSUMREC' +  checksum
        seqnumber = rcv[0:18]
        seqnumber1 = rcv[2:18]
        print 'SEQ:' + seqnumber1
        data = rcv[18:len(rcv)-128][2:].zfill(6976)
        print 'data' + data
        new_checksum = crc32(seqnumber1+data)
        # new_checksum = (hashlib.md5(seqnumber1+data).hexdigest())
        new_checksum = bin(int(new_checksum, 16))[2:].zfill(128)
        continue
    else:
        continue
    true = '0b0000000000000000'
    false  ='0b1111111111111110'

    if new_checksum != checksum:
        print 'Send NAK'
        t.sendbits(false)
        continue
   
    else:
        t.sendbits(true)
        print 'Send ACK'
        print data
        # output the rcv to the output file
        output.write(bits2string(data))
        continue
    print 'seqnumber:' + seqnumber + '\n'
    print 'data:' + data + '\n'
    # print 'checksum:' + checksum + '\n'
    
    # output.close()

    # check if packet corrupt: checksum

    # check if correct segment was rcved

	# check to see if the seqnumber is correct
 
