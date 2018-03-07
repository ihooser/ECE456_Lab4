'''
Created on Mar 2, 2018

@author: ihooser
'''

def encrypt(num, datain):
    t = list(datain)
    if len(datain)%2 == 0:
        for x in range(0, len(datain),2):
#             print t
            temp1 = t[x]
            temp2 = ord(t[x+1])
            temp3 = int(num)
            temp4 = temp2 ^temp3
            t[x] = chr(temp4)
            t[x+1] = temp1

    else:
         for x in range(0, len(datain)-1,2):
            temp1 = t[x]
            temp2 = ord(t[x+1])
            temp3 = int(num)
            temp4 = temp2 ^temp3
            t[x] = chr(temp4)
            t[x+1] = temp1
#           print t
    
    if len(datain)%2 != 0:
        lneth = len(datain) 
        temp2 = ord(t[lneth-1])
        temp3 = int(num)
        temp4 = temp2 ^temp3
        t[lneth-1] = chr(temp4)
#       print t
    fini = ''.join(t)
    return fini

import sys
import socket
import datetime
import time
from time import gmtime, strftime


if __name__ == '__main__':
    pass

s=socket.socket (socket.AF_INET, socket.SOCK_DGRAM,0)
ti = strftime(" Day sent: %Y-%m-%d", gmtime())
t = datetime.datetime.time(datetime.datetime.now())
print ti,"Time ", t
#need ip to knnow who send the data
sock = socket.gethostbyname(socket.gethostname())
print "The ip address that is used is:", sock
client_port = "6001"
print " The client port-number is: ", client_port
#reading in all the imputs
client_number = sys.argv[1]
serverIP = sys.argv[2]
serverPort = int(sys.argv[3])
datafile = sys.argv[4]
key = sys.argv[5]
#choosing if data is from keyboard or file
inputFrom = raw_input('will the data come from a file(y/n):')
if inputFrom == 'y':
    code_location = sys.argv[0]
    date = open(datafile,"r")
    datain =date.read()
    print datain
else:
    datain = raw_input('Enter your input:')
    print datain

print "The server IP is:", serverIP
print "The server Port is:", serverPort

 
encrypted = encrypt(5, datain)
print encrypted
#combining all the imformation into one sting to send
Message = client_number + " The client ip-address: " + sock + " The client port-number: " + client_port + str(ti) + " Time sent: " + str(t)+ " Data: " + encrypted
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock.sendto(Message, (serverIP, serverPort))
while True:
    print "WAITING!!!!!!!!!! for server"
    data, server = clientSock.recvfrom(1024)
    print  data






