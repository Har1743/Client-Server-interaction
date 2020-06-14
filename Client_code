import socket
import sys


# This function creates the socket using IPV4 addressing and TCP protocol

def create_socket():

    try:
        print("\n*** Creating the socket ... ***")
        global client_socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print("Socket error in socket.socket() ", socket.error)
        client_socket = None
    else:
        print("<<< Socket created >>>")


# This function checks whether the entered IP is valid or not

def check_ip():

    global host
    host = input("Enter the IP address for connecting to the server : ")

    try:
        socket.inet_aton(host)
    except socket.error:
        print("Entered IP address is not a valid IP")
        print("Retrying ...")
        check_ip()


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


# This function connects to the server

def connection():

    try:
        client_socket.connect((host, int(port)))
    except socket.error:
        print("Connection error", socket.error)
        sys.exit()


# This calls the create_socket() to create a socket
create_socket()

# This calls the check_ip for the validation of the IP
check_ip()

# You have enter the port number on which the socket binds
port = input("\nEnter the port [ range b/w 2000-8999 ] for binding the socket : ")

# This calls the check_port() to check the port number validation
check_port(port)

# This calls the connection() to connect with the server
connection()


print("Connected with ", str(host))

print("\n\n*************************")
print("START YOUR CONVERSATION WITH THE SERVER")

# Firstly assign value of msg to null
msg = ""

while True:
    # accepting the messages from the server
    try:
        msg_server = client_socket.recv(1024)
        if len(msg_server) == 0:
            print("Connection closed by the server ", str(host))
            sys.exit()
    except socket.error:
        print("Error in accepting messages from the sever", socket.error)

    else:
        print("server >>>>> ", msg_server.decode())

    # Client sending the messages to the server
    try:
        client_socket.sendall(input("client >>>>> ").encode())
    except socket.error:
        print("Error in sending message in sendall", socket.error)

# This function closes the socket
client_socket.close()
