"""
CME 334
Lab 2 - Exercise 2.1 (server)
Thursday February 3 2022

Tyrel Kostyk
tck290
11216033
"""

import socket
import sys

# create an IPv4 TCP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set address and port number of host server
host, port = socket.gethostname(), 30123

# set max buffer size for data transmission
bufferSize = 4096

# attempt to bind to the socket
try:
	serverSocket.bind((host, port))
except socket.error as msg:
	print("Binding failed, Error code: " + str(msg[0]) + ", Message: " + msg[1])
	sys.exit()
print("Binding complete")

# begin listening; allow up to 5 queued connections
serverSocket.listen(5)
print("Socket listening")

while True:
	# establish a TCP connection (blocking call)
	clientSocket, addr = serverSocket.accept()

	with clientSocket:
		print("Connection established at ", addr)

		while True:
			# receive data from client
			data = clientSocket.recv(bufferSize)

			# TODO: add current server time to echo message

			# echo data back to client
			error = clientSocket.sendall(data)
