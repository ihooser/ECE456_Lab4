'''
Created on Mar 2, 2018

@author: ihooser
'''
def encrypt(num, datain):
    t = list(datain)
    print datain
    #this is for when the data length is even
    if len(datain)%2 == 0:
        for x in range(len(datain)-2,-2,-2):
#             print t
            temp1 = t[x+1]
            temp2 = ord(t[x])
            temp3 = int(num)
            temp4 = temp2 ^temp3
            t[x+1] = chr(temp4)
            t[x] = temp1
    #this is for when it is odd
    else:
         for x in range(len(datain)-3,-1,-2):
#             print t
            temp1 = t[x+1]
            temp2 = ord(t[x])
            temp3 = int(num)
            temp4 = temp2 ^temp3
            t[x+1] = chr(temp4)
            t[x] = temp1

    #this takes care of the last chareter in an odd length data
    if len(datain)%2 != 0:
        print "_______________________________"
        lenth = len(datain) 
        temp2 = ord(t[lenth-1])
        temp3 = int(num)
        temp4 = temp2 ^temp3
        t[lenth-1] = chr(temp4)
#         print t
    fini = ''.join(t)
    return fini

def prints(data,stack1,stack2,stack3,stack4,stack5):
    #making my own stack of size five
    stack5 = stack4
    stack4 = stack3
    stack3 = stack2
    stack2 = stack1
    stack1 = data
    send_Back = "Message1: " + stack1 + "\nMessage2: " + stack2 + "\nMessage3: " + stack3 + "\nMessage4: " + stack4 + "\nMessage5: " + stack5
    print send_Back
    s = data.split()
    return (send_Back,stack1,stack2,stack3,stack4,stack5)


import re
import socket
import sys
if __name__ == '__main__':
    pass

keys = open("keys.txt","r")
p =keys.read()
keys = re.findall(r'\b\d+\b',p)
# keys =[5,8,63,2]
print keys
UDP_PORT_NO = int(sys.argv[1])
stack1 = ""
stack2 = ""
stack3 = ""
stack4 = ""
stack5 = ""
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#getting the ip of the Server
sock = socket.gethostbyname(socket.gethostname())
UDP_IP_ADDRESS = sock
#binding together the ip and the port for this server
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
while True:
    print "WAITING for client"
    data, addr = serverSock.recvfrom(1024)
    data_read = data.split()
    client_number = int(data_read[0])
    #this is to get only receive data for amount of clients there is data for
    if client_number <=len(keys):
        key = keys[int(client_number)-1]
        print "the key being used for client", client_number, " is key ", key
        data_code = " ".join(data_read[16:])
        data_temp = encrypt(key,data_code)
        print "this is the decoded data: ", data_temp
        data = data.replace(data_code,data_temp)
        print data
        send_Back,stack1,stack2,stack3,stack4,stack5 = prints(data,stack1,stack2,stack3,stack4,stack5)
    #if there is no data then the error is sent back
    else: 
        key = 0
        print "There is no key for this client"
        data_code = " ".join(data_read[16:])
        data_temp = "There is no key to decrypt this data"
        print data_temp
        send_Back = data_temp
        
    if data:
        sent = serverSock.sendto(send_Back, addr)
        print sys.stderr, 'sent %s bytes back to %s' % (sent, addr)
#     print " the data has been sent out"
