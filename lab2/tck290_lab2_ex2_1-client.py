"""
CME 334
Lab 2 - Exercise 2.1 (client)
Thursday February 3 2022

Tyrel Kostyk
tck290
11216033
"""

import socket
import sys

# create an IPv4 TCP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get address and port number of host server
host, port = socket.gethostname(), 30123

# set max buffer size for data transmission
bufferSize = 4096

# connect to the host server
clientSocket.connect((host, port))

while True:
	# read from stdin
	data_out = bytes(input(">> "), "utf-8")

	# send message
	error = clientSocket.sendall(data_out)

	if error is not None:
		print("Client: Error on sendall")
		break

	# receive the echo'd message
	data_in = clientSocket.recv(bufferSize)

	if not data_in:
		print("Client: Error on recv")
		break

	print(data_in.decode("utf-8"))
