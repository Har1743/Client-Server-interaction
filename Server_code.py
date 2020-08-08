import socket
import sys


# This function creates the socket using IPV4 addressing and TCP protocol

def create_socket():

    try:
        print("\n*** Creating the socket ... ***")
        global server_socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print("Socket error in socket.socket() ", socket.error)
        print("Retrying ...")
        server_socket = None
        create_socket()
    else:
        print("<<< Socket created >>>")


# This function checks whether entered port number is valid or not

def check_port(port):

    if (port.isnumeric()) == True:
        if (int(port) > 1999) and (int(port) < 9000):
            print("Entered port number valid to be used")
        else:
            print("Entered port number is out of range")
            print("Exiting the server ...")
            sys.exit()
    else:
        print("Entered port number is not numeric")
        print("Exiting the server ...")
        sys.exit()


# This function binds the socket

def bind_socket():

    try:
        host = socket.gethostname()
        print("\n*** Binding the socket for " + str(host) + " on the port " + str(port) + " ... ***")
        server_socket.bind(('0.0.0.0', int(port)))
    except socket.error:
        print("Binding error in bind() ", socket.error)
        print("Retrying ...")
        bind_socket()
    else:
        print("<<< Binding of socket successful waiting for connection to establish ... >>>")


# This function accepts the client's request

def accepting():

    global client_socket, client_address
    try:
        client_socket, client_address = server_socket.accept()
    except socket.error:
        print("Problem in accepting the request from the user", socket.error)
        print("Retrying ...")
        accepting()


# This calls the create_socket() to create a socket
create_socket()

# You have enter the port number on which the socket binds
port = input("\nEnter the port [ range b/w 2000-8999 ] for binding the socket : ")

# This calls the check_port() to check the port number validation
check_port(port)

# This call the bind_socket() to bind the socket
bind_socket()

# socket started listening for the connections
server_socket.listen(5)

# This calls the accepting() to accept the connection
accepting()

print("Connected with ", client_address[0])

print("\n\n*************************")
print("START YOUR CONVERSATION WITH THE CONNECTED CLIENT")

# Firstly assign value of msg to null
msg = ""

while True:
    # Server sending the message to the client
    try:
        client_socket.sendall(input("server >>>>> ").encode())
    except socket.error:
        print("Error in sending message in sendall", socket.error)

    # Server accepting the messages from the client
    try:
        msg_client = client_socket.recv(1024)
        if len(msg_client) == 0:
            print("Connection closed by the Client ", client_address[0])
            sys.exit()
    except socket.error:
        print("Error in accepting the message from the Client", socket.error)
    else:
        print("client >>>>> ", msg_client.decode())

# This function closes the socket
server_socket.close()

