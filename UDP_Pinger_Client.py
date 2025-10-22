# Student Name: Hettiarachchige Mary Shenara Amodini De Silva
# Student ID: 14545786
# Assignment: Project_B
# Network Fundamentals (CINEF001)

# UDP_Pinger_Client.py

import random
import time
from socket import *

# Server configuration
serverName = 'localhost'
serverPort = 12000

# Creates UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set a one-second timeout
clientSocket.settimeout(1)

# Number of pings to send
numOfPings = 10

# Variables for RTT calculations
rttTimes = []

def send_ping(sequence_number):
    # Format the ping message
    ping_message = f'Ping {sequence_number} {time.time()}'
    startTime = time.time()

    # Send ping message to the server
    clientSocket.sendto(ping_message.encode(), (serverName, serverPort))

    try:
        # Receive the response message
        response, serverAddress = clientSocket.recvfrom(1024)
        endTime = time.time()

        # Calculte round trip time
        rtt = endTime - startTime
        rttTimes.append(rtt)

        print(f'Ping to {serverName}, Ping #{sequence_number}, RTT: {rtt:.6f} seconds')

    except timeout:
        # Handle timeout
        print(f'Ping to {serverName}, Ping #{sequence_number}, Request Timed Out')

# Main loop for sending pings
for sequence_number in range(1, numOfPings + 1):
    send_ping(sequence_number)

# Calculate RTT statistics
if rttTimes:
    minimum_rtt = min(rttTimes)
    maximum_rtt = max(rttTimes)
    average_rtt = sum(rttTimes) / len(rttTimes)
    packet_loss_rate = ((numOfPings - len(rttTimes)) / numOfPings) * 100

else:
    minimum_rtt = 0
    maximum_rtt = 0
    average_rtt = 0
    packet_loss_rate = 100

# Print RTT statistics
print(f'\nRTT Statistics for {serverName}:')
print(f'Min RTT: {minimum_rtt:.6f} seconds')
print(f'Max RTT: {maximum_rtt:.6f} seconds')
print(f'Average RTT: {average_rtt:.6f} seconds')
print(f'Packet Loss Rate: {packet_loss_rate:.2f}%')

# Close the socket
clientSocket.close()

