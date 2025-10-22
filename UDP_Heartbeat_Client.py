# Student Name: Hettiarachchige Mary Shenara Amodini De Silva
# Student ID: 14545786
# Assignment: Project_B
# Network Fundamentals (CINEF001)

# UDP_Heartbeat_Client.py

import socket
import time

class UDPHeartbeatClient:
    def __init__(self, serverName, serverPort, clientName, clientPort, total_heartbeats=10):
        self.serverName = serverName
        self.serverPort = serverPort
        self.clientName = clientName
        self.clientPort = clientPort
        self.total_heartbeats = total_heartbeats
        self.sequenceNumber = 0
        self.clientSocket = None

    def setup_client_socket(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.clientSocket.bind((self.clientName, self.clientPort))

    def send_heartbeats(self):
        while self.sequenceNumber < self.total_heartbeats:
            timestamp = time.time()
            message = f"{self.sequenceNumber},{timestamp}"
            self.clientSocket.sendto(message.encode("utf-8"), (self.serverName, self.serverPort))

            print(f"Sent heartbeat to server, Sequence #{self.sequenceNumber}, Timestamp: {timestamp:.4f}")

            time.sleep(1)
            self.sequenceNumber += 1

    def close_client_socket(self):
        if self.clientSocket:
            self.clientSocket.close()

    def run(self):
        self.setup_client_socket()
        self.send_heartbeats()
        self.close_client_socket()

if __name__ == "__main__":
    client = UDPHeartbeatClient(serverName="localhost", serverPort=12000, clientName="localhost", clientPort=12001)
    client.run()
