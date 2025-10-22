# Student Name: Hettiarachchige Mary Shenara Amodini De Silva
# Student ID: 14545786
# Assignment: Project_B
# Network Fundamentals (CINEF001)

# UDP_Pinger_Server.py
# We will need the following module to generate randomise lost packets

import random
from socket import *
serverName = 'localhost'     # Input IP address
# serverPort = '12000'

# Create UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP addresses and port number to the socket
serverSocket.bind((serverName, 12000))
print('The server is running on ' + serverName)

while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)

    # Receive the client packet along with the address it is coming from save as message
    message, address = serverSocket.recvfrom(1024)

    # Capitalize the message from the client
    message = message.upper()

    # If rand is less than 4, we consider the packet lost and do not respond
    if rand < 4:
        continue

    # Otherwise, the server responds
    serverSocket.sendto(message, address)
