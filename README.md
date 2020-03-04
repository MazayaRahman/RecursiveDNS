Siddhi Kasera(smk339) & Mazaya Rahman(mr1411)

1. Implementation of Recursive Client Functionality

We created two servers, ts and rs and one client. The rs and ts servers both create their own DNS tables of hostnames and ip addresses from the files in a 2d array structure.  They listen for client connections and look up queried hostnames from their tables, and send back their corresponding ip to the client.  
The client takes in the hostname on which the servers are running as input. The client reads a file that consists of the hostnames. For each hostname, the client creates a new socket to connect to the rs server. After connecting, it sends the queried hostname to the rs server. The rs server searches if it has that hostname in its DNS table. If yes, it sends the hostname alongside ‘A’. If the rs server does not find the queried hostname it sends the ts hostname alongside ‘NS’. The client connects to the ts server using the ts hostname to look for the queried hostname. If the ts finds the hostname,  it sends the client the hostname alongside ‘A’, otherwise an error indicating the hostname was not found.
This is a recursive functionality since we are treating the client as the local DNS server.The client acts as a DNS server and recursively gathers the info necessary and gives the asking client the answer.


3. Problems faced while developing the code.
We had trouble in the beginning connecting our client to multiple servers using the same socket. We then realized that we cannot reuse the socket and thus created a new socket for each connection.
Another problem we faced was that our servers stopped listening after one connection from the client. We then decided to accept connections in a loop so it can accept multiple connections.

4.Lesson from the project
We got a more concrete knowledge of how DNS works. We also learned how to connect the client to multiple different servers running on different machines. 
