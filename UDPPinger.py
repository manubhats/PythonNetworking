__author__ = 'Manu Bhat'

import socket
from socket import AF_INET, SOCK_DGRAM
from datetime import datetime


print 'Client is ready to ping the server.........'
#localhost IP
serverName = '127.0.0.1'
#create the socket
clientSocket = socket.socket(AF_INET,SOCK_DGRAM)
#sets the timeout at 1 second
clientSocket.settimeout(1)
#variable to keep track of the ping count
pingno = 1
while pingno <= 10:
    message = 'Ping success'
    #gives current time
    start = datetime.now()
    #sends a message to the server on port number 9876
    clientSocket.sendto(message,(serverName, 9876))
    try:
        print 'Ping number: ', pingno
        #recieving message from server
        message, address = clientSocket.recvfrom(1024)
        end = datetime.now()
        # calculating how much time has elapsed since the start time
        elapsed = end - start
        #print 'Start time is: ' , start
        print 'Reply from server: ' ,message
        #print 'End time is: ' , end
        print 'Round Trip Time(RTT) is ',elapsed.seconds,'Seconds,',elapsed.microseconds,'Microseconds'
        print '____________________________________'
        pingno+=1
    #if the socket takes longer that 1 second, it does the following instead
    except socket.timeout:
        print 'Request timed out'
        print '____________________________________'
        #ping count is increased after all of the other statements in the while
        pingno+=1

    #closes the socket after 10 packets
    if pingno > 10:
        clientSocket.close()
