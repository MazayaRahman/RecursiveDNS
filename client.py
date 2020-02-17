import sys
import socket as mysoc
import threading

#client task
def client(host, port):
    print 'host: ', host, 'port: ', port

    try:
        cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))

    port = int(port)
# Define the port on which you want to connect to the server
    sa_sameas_myaddr =mysoc.gethostbyname(host)
# connect to the server on local machine
    server_binding=(sa_sameas_myaddr,port)
    cs.connect(server_binding)

    
    cs.close()

    exit()

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
host = sys.argv[1]
port = sys.argv[2]
print 'host: ', host, 'port: ', port
t2 = threading.Thread(name='client', target=client, args=(host,port,))
t2.start()
t2.join()
exit()
