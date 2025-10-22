# Student Name: Hettiarachchige Mary Shenara Amodini De Silva
# Student ID: 14545786
# Assignment: Project_B
# Network Fundamentals (CINEF001)

# UDP_Heartbeat_Server.py

import socket
import time

class UDPHeartbeatServer:
    def __init__(self, serverName, serverPort, client_timeout=5):
        self.serverName = serverName
        self.serverPort = serverPort
        self.client_timeout = client_timeout
        self.last_timestamps = {}

    def start_server(self):
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        serverSocket.bind((self.serverName, self.serverPort))

        print(f"UDP Heartbeat server listening on {self.serverName} port: {self.serverPort}")

        while True:
            data, address = serverSocket.recvfrom(1024)
            self.handle_heartbeat(data, address)

    def handle_heartbeat(self, data, address):
        receive_time = time.time()
        message = data.decode("utf-8")
        sequenceNumber, timestamp = message.split(",")
        sequenceNumber = int(sequenceNumber)
        timestamp = float(timestamp)

        time_difference = receive_time - timestamp

        if sequenceNumber == 0:
            print("Received first heartbeat from client.")

        print(f"Received heartbeat from client {address}, Sequence #{sequenceNumber} with Time Difference: {time_difference:.4f} seconds")

        self.update_timestamp(address, receive_time)
        self.check_lost_clients(receive_time)
        self.check_missing_heartbeats(sequenceNumber, time_difference)

    def update_timestamp(self, address, timestamp):
        self.last_timestamps[address] = str(timestamp)

    def check_lost_clients(self, receive_time):
        clients_to_remove = []

        for clientAddress, last_timestamp in self.last_timestamps.items():
            try:
                last_timestamp_float = float(last_timestamp)
            except ValueError:
                print(f"Invalid timestamp for client {clientAddress}: {last_timestamp}")
                continue  # Skip if the timestamp is not a valid float

            if receive_time - last_timestamp_float > self.client_timeout:
                print(f"Client {clientAddress} has stopped (no heartbeat received for {self.client_timeout} seconds)")
                clients_to_remove.append(clientAddress)

        # Remove the lost clients after iterating over the dictionary
        for clientAddress in clients_to_remove:
            del self.last_timestamps[clientAddress]

    def check_missing_heartbeats(self, sequenceNumber, time_difference):
        expected_sequence_number = max(0, sequenceNumber - 1)
        received_sequence_numbers = {int(s.split(",")[0]) for s in self.last_timestamps.values() if
                                     "." in s and s.split(",")[0].isdigit()}

        for missing_sequence_number in range(expected_sequence_number, sequenceNumber):
            if missing_sequence_number not in received_sequence_numbers:
                print(f"Missing heartbeat from Sequence #{missing_sequence_number} with Time difference {time_difference:.4f} seconds")


if __name__ == "__main__":
    server = UDPHeartbeatServer(serverName="localhost", serverPort=12000)
    server.start_server()
