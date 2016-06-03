from socket import *

# Create a server socket
#Bind to port 8899
serverPort = 1989
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    # Connection
    print 'Server is up and running...Ready to accept requests'
    connSock, adrss = serverSocket.accept()
    print 'Connection request from this address ', adrss
    message = connSock.recv(1024)

    # Check the file name
    print message.split()[1]
    filename = message.split()[1].partition("/")[2]
    f_exist = "false"
    filedir = "/" + filename
    try:
        f = open(filedir[1:], "r")
        opdata = f.readlines()
        f_exist = "true"
        print 'File fetched successfully!'
        # Send an HTTP header line into the socket
        connSock.send("HTTP/1.0 200 OK\r\n")
        connSock.send("Content-Type:text/html\r\n")
        # Send the content of the requested file to the client
        for i in range(0, len(opdata)):
            connSock.send(opdata[i])
        # Error handling
    except IOError:
        print 'File Exist: ', f_exist
        if f_exist == "false":
            connSock.send('\n404 - File Not Found\n')
            connSock.send('\n Verify the URL and try again!!\n')   
            print "File not found!!!"
            print "Please verify the file path and use this format"
            print "http://localhost:[portno]/filename"
        
    # Close the socket
    connSock.close()
   



