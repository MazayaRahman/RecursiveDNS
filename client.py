import sys
import socket as mysoc
import threading

#client task
def client(host, rsport, tsport):
    print 'host: ', host, 'rsport: ', rsport, 'tsport: ', tsport

    rsport = int(rsport)
    tsport = int(tsport)

    for hn in hostname:
       # create client socket and connect to RS
       try:
           cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
           #cs1 = mysoc.socket(sysoc.AF_INET, mysoc.SOCK_STREAM)
           print("[C]: Client socket created")
       except mysoc.error as err:
           print('{} \n'.format("socket open error ",err))
           #cs1=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
       print("the hostname is:" ,hn)
       sa_sameas_myaddr = mysoc.gethostbyname(host)
       server_binding = (sa_sameas_myaddr, rsport)
       cs.connect(server_binding)
       print ("the hn sending is: ", hn)
       # convert to lowercase
       hn = hn.lower()
       cs.send(hn.encode('utf-8'))
       data_from_rs = cs.recv(100).decode('utf-8') #data received from rs server.
       print("the data from rs is:", data_from_rs)
       status = data_from_rs.split(' ')
       #print(status[2])
       if(status[2] == 'A'):
           print(data_from_rs)
       #if(status[2] == 'NS'):
       cs.close()

       # Create a client socket to connect to TS
       if(status[2] =='NS'):
           print("here")
           tsHost = status[0];
           try:
               cs = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
               print("Client socket1 created")
           except mysoc.error as err:
               print('{} \n'.format("socket open error ",err))
           #connecting to loca ts for now
           sa_sameas_myaddr = mysoc.gethostbyname(tsHost)
           server_binding = (sa_sameas_myaddr, tsport)
           cs.connect(server_binding)
           print("the hn sending is: ", hn)
           cs.send(hn.encode('utf-8'))
           data_from_ts = cs.recv(100).decode('utf-8')  #data received from ts server
           print("data from ts is:" , data_from_ts)
           cs.close()

       # signal servers to close
       # close rs
    try:
        cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
         #cs1 = mysoc.socket(sysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))
        #cs1=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    print("the hostname is:" ,hn)
    sa_sameas_myaddr = mysoc.gethostbyname(host)
    server_binding = (sa_sameas_myaddr, rsport)
    cs.connect(server_binding)
    print ("Sending message: ", "END")
    # convert to lowercase
    message = "END"
    cs.send(message.encode('utf-8'))
    cs.close
    #close ts 
    if(tsHost):
        try:
             cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
             #cs1 = mysoc.socket(sysoc.AF_INET, mysoc.SOCK_STREAM)
             print("[C]: Client socket created")
        except mysoc.error as err:
             print('{} \n'.format("socket open error ",err))
             #cs1=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("the hostname is:" ,hn)
        sa_sameas_myaddr = mysoc.gethostbyname(tsHost)
        server_binding = (sa_sameas_myaddr, tsport)
        cs.connect(server_binding)
        print ("Sending message: ", "END")
        # convert to lowercase
        message = "END"
        cs.send(message.encode('utf-8'))
        cs.close


    exit()

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
host = sys.argv[1]
rsport = sys.argv[2]
tsport = sys.argv[3]
print 'host: ', host, 'rsport: ', rsport, 'tsport: ', tsport
hostname =[]
with open("PROJI-HNS.txt", 'r') as f:
    for lines in f:
        #print(lines)
        hostname.append(lines.strip())

    for i in hostname:
        print("The  hostname is:", i)
#print("The second hostname is:", hostname[1])

t2 = threading.Thread(name='client', target=client, args=(host,rsport,tsport,))
t2.start()
t2.join()
exit()
