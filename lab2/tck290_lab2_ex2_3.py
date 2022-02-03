"""
CME 334
Lab 2 - Exercise 2.3 (web server client)
Thursday February 3 2022

Tyrel Kostyk
tck290
11216033
"""

import socket
import sys

# get address, port number, and file name for the upcoming request
host = sys.argv[1]
port = int(sys.argv[2])
file = sys.argv[3]

request_type = "GET"
http_version = "HTTP/1.1"

# set max buffer size for data transmission
bufferSize = 4096

# create an IPv4 TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:

	# connect to the host server
	clientSocket.connect((host, port))

	# build request header
	req = request_type + " /" + file + " " + http_version + "\r\n\r\n"

	# send request header
	error = clientSocket.sendall(req.encode("utf-8"))

	if error is not None:
		print("Client: Error on sending GET request for file " + file)
		sys.exit()

	while True:
		# receive the reponse
		data_in = clientSocket.recv(bufferSize)

		# exit once the connection is closed (full webpage has been received)
		if not data_in:
			sys.exit()

		# print the response to stdout
		print(data_in.decode("utf-8"))
