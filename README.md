## UDP PINGER PROJECT

A Python-based project that simulates network communication using the User Datagram Protocol (UDP). The system sends and receives packets, measures round-trip time (RTT), and calculates packet loss to analyze network performance and reliability.

---

## Overview

The UDP Pinger project demonstrates how UDP works as a connectionless transport protocol. It includes both a client and a server that exchange packets to test network latency and reliability. The system can also simulate packet loss and delayed responses to mimic real-world network conditions.

---

## Features

- Implements UDP client and server communication  
- Measures round-trip time (RTT) for each packet  
- Calculates average delay and packet loss rate  
- Simulates packet loss and timeout scenarios  
- Helps visualize UDP’s unreliable yet fast data transmission  

---

## Technologies Used

- Python  
- Socket Programming  
- Networking Fundamentals  

---

## How to Run

1. Clone the repository:
   ```bash
     git clone https://github.com/yourusername/UDP-Pinger.git

2. Navigate to the project directory:
   ```bash
     cd <directory_name>

4. Run the server first:
   ```bash
     python UDP_Pinger_Server.py

6. In another terminal, run the client:
   ```bash
     python UDP_Pinger_Client.py

---

## Learning Outcomes

- Understanding of UDP and its characteristics
- Implementation of client-server communication
- Measurement of network latency and packet loss
- Insights into real-time system monitoring and reliability
