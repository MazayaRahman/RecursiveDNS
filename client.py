import sys
import socket as mysoc
import threading

#client task
def client(host, port):
    print 'host: ', host, 'port: ', port



    port = int(port)
# Define the port on which you want to connect to the server
    #sa_sameas_myaddr =mysoc.gethostbyname(host)
# connect to the server on local machine
    #server_binding=(sa_sameas_myaddr,port)
    #cs.connect(server_binding)
    for hn in hostname:
       try:
           cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
           #cs1 = mysoc.socket(sysoc.AF_INET, mysoc.SOCK_STREAM)
           print("[C]: Client socket created")
       except mysoc.error as err:
           print('{} \n'.format("socket open error ",err))
           #cs1=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
       print("the hostname is:" ,hn)
       sa_sameas_myaddr = mysoc.gethostbyname(host)
       server_binding = (sa_sameas_myaddr, port)
       cs.connect(server_binding)
       print ("the hn sending is: ", hn)
       cs.send(hn.encode('utf-8'))
       data_from_rs = cs.recv(100) #data received from rs server.
       print("the data from rs is:", data_from_rs)
       status = data_from_rs.split(' ')
       #print(status[2])
       if(status[2] == 'A'):
           print(data_from_rs)
       #if(status[2] == 'NS'):
       cs.close()

    exit()

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
host = sys.argv[1]
port = sys.argv[2]
print 'host: ', host, 'port: ', port
hostname =[]
with open("PROJI-HNS.txt", 'r') as f:
    for lines in f:
        #print(lines)
        hostname.append(lines.strip())

    for i in hostname:
        print("The  hostname is:", i)
#print("The second hostname is:", hostname[1])

t2 = threading.Thread(name='client', target=client, args=(host,port,))
t2.start()
t2.join()
exit()
