# Client-Server-interaction

This is python program based client server interaction program which helps you client to interact with the server..

BASIC IMPORT MODULES :-

Import socket :-

To create a socket, you must use the socket.socket() function available in socket module, which has the general syntax −

# Socket functions used

### Create a socket object. s = socket.socket()  
s = socket.socket (socket_family, socket_type, protocol=0)

### s.bind()
Define the port on which you want to connect. port = 12345.
This method binds address (hostname, port number pair) to socket.

### s.listen()
This method sets up and start TCP listener.

### s.accept()
This passively accept TCP client connection, waiting until connection arrives (blocking).

### s.connect()
This method actively initiates TCP server connection.

### s.recv()
This method receives TCP message

### s.send()
This method transmits TCP message

### s.recvfrom()
This method receives UDP message

### s.sendto()
This method transmits UDP message

### s.close()
This method closes socket

Import sys :-
The python sys module provides functions and variables which are used to manipulate different parts of the Python Runtime Environment. It lets us access system-specific parameters and functions.

# BASIC FUNCTIONS used :--

### print ( ) :-
The print() function prints the specified message to the screen, or other standard output device. The message can be a string, or any other object, the object will be converted into a string before written to the screen.

### input ( ) :-
The function input() input has an optional parameter, which is the prompt string. If the input function is called, the program flow will be stopped until the user has given an input and has ended the input with the return key.

# Advantages 

1. It is bidirectional user and client both can send and receive messages. 
2. We dont need to enter exit or any other just do (ctrl+c) to close the connection. 
3. It is all based on an exception handling concept so if there is any human or connection error it will pop up with an exception.

# Disadvantages

1. It is not multithreaded so it can only establish one connection at a time with a sequence [send] [receive] [send] [receive].
2. It is not GUI based.
3. It can only support IPv4 based connections.
