import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        self.connections[connection_id]=connection_load
        # Add the connection to the dictionary with the calculated load

    def close_connection(self, connection_id):
        del self.connections[connection_id]
        # Remove the connection from the dictionary

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for n in self.connections.values(): 
            total += n
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())
    
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        self.ensure_availability()
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
        self.connections[server] = connection_id
        # Add the connection to the server
        server.add_connection(connection_id)

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        for server,connections in self.connections.items():
            if connection_id in connections:
                    delserver = server
                
        # Close the connection on the server
        delserver.close_connection(connection_id)
        print(self.connections)
        
        # Remove the connection from the load balancer
        del self.connections[delserver]
        print(self.connections)
                     
    def avg_load(self):
        """Calculates the average load of all servers"""
        total_load = 0
        n = 0
        for server in self.servers:
            total_load += server.load()
            n += 1            
        return total_load/n

    def ensure_availability(self):
        if self.avg_load() > 50:
            self.servers.append(Server())
            return print("New server added" + "{:>8}".format(" ") +" | " + "{:.2f}".format(self.avg_load()))
        return print("Added to existing server" + " | " + "{:.2f}".format(self.avg_load()))

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))


server = Server()
server.add_connection("192.168.1.1")
print(server.load())

server.close_connection("192.168.1.1")
print(server.load())

l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())

l.servers.append(Server())
print(l.avg_load())

l.close_connection("fdca:83d2::f20d")
print(l.avg_load())

for connection in range(30):
    l.add_connection(connection)
