import sys
import socket as mysoc
import threading

# Looks up the target host in the dns table and returns the entry
def lookup(target):
    for entry in dns_table:
        hn = entry[0].lower()
        if hn == target:
            print "found!"
            print entry
            entry = ' '.join(entry)
            #print entry
            return entry
    # Did not find hostname, find TS gethostname
    error = target + " - Error:HOST NOT FOUND"
    return error


# server task
def server(port):
    try:
        ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))

    port = int(port)
    server_binding=('',port)
    ss.bind(server_binding)
    ss.listen(1)
    host=mysoc.gethostname()

    print("[S]: Server host name is: ",host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ",localhost_ip)


    # Listen for connections from client
    while(True):
        # accept client
        csockid, addr = ss.accept()
        print ("[S]: Got a connection request from a client at", addr)
        hostname = csockid.recv(100).decode('utf-8')
        #print hostname
        if not hostname:
            break
        print("[S]: Data received from client::  ",hostname.decode('utf-8'))
        print hostname
        if(hostname == "END"):
            ss.close
            exit()
        #Look in the table
        record = lookup(hostname)
        if not record:
            print "TS Hostname not found!"

        # Send entry back to Client
        print("[S]: Data sent to client ::  ",record)
        csockid.send(record.encode('utf-8'))


    # close server socket
    ss.close()
    exit()

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
port = sys.argv[1]
print 'port: ', port
fp = open("PROJI-DNSTS.txt", "r")
lines = fp.readlines()
dns_table = []
for line in lines:
    entry = line.strip().split(' ')
    dns_table.append(entry)

for entry in dns_table:
    print entry
t1 = threading.Thread(name='server', target=server, args=(port,))
t1.start()

t1.join()

exit()
