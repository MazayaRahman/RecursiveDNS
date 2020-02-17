import sys
import socket as mysoc
import threading

def server(port):
    try:
        ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))

    port = int(port)
    server_binding=('',port)
    print server_binding
    ss.bind(server_binding)
    ss.listen(1)
    host=mysoc.gethostname()
    #hi
    print("[S]: Server host name is: ",host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ",localhost_ip)

    # accept client
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at", addr)
    # create a thread to handle communication with accepted client


    # close server socket
    ss.close()
    exit()

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
port = sys.argv[1]
print 'port: ', port
t1 = threading.Thread(name='server', target=server, args=(port,))
t1.start()

t1.join()

exit()
