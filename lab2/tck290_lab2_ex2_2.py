"""
CME 334
Lab 2 - Exercise 2.2 (web server)
Thursday February 3 2022

Tyrel Kostyk
tck290
11216033
"""

import socket
import sys
import os.path

# set address and port number of host server
host, port = "localhost", 8080

# set max buffer size for data transmission
bufferSize = 4096

# set location of error file
errorFile = "tck290_lab2_page_error.html"

# create an IPv4 TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:

	# attempt to bind to the socket
	try:
		serverSocket.bind((host, port))
	except socket.error as msg:
		print("Binding failed, Error code: " + str(msg[0]) + ", Message: " + msg[1])
		sys.exit()
	print("Binding complete")

	# begin listening; allow up to 5 queued connections
	serverSocket.listen(5)
	print("Web Server hosting at " + str(host) + ":" + str(port))

	while True:
		# establish a TCP connection (blocking call)
		clientSocket, addr = serverSocket.accept()

		with clientSocket:
			print("Connection established at ", addr)

			# receive data from client
			data_in = clientSocket.recv(bufferSize)

			# exit on error
			if not data_in:
				print("Server: Error on recv")
				break

			# extract request type and filename from HTTP request
			req = data_in.decode("utf-8")
			fields = req.split("\r\n")
			request, file, version = fields[0].split(' ')
			# remove leading slash
			file = file[1:]

			print(request + " request received for file: " + file + " with HTTP Version " + version)

			# TODO: ensure file exists
			if (os.path.isfile(file)):
				# construct header
				resp = version + " 200 OK\r\n\r\n"
				# send header
				error = clientSocket.sendall(resp.encode("utf-8"))

				if error is not None:
					print("Server: Error on sending 200 OK")
					break

				# open and send file
				with open(file, 'rb') as f:
					error = clientSocket.sendall(f.read(bufferSize))

					if error is not None:
						print("Server: Error on sending page")
						break

					endOfFile = "\r\n"
					error = clientSocket.sendall(endOfFile.encode("utf-8"))

					if error is not None:
						print("Server: Error on sending end of page")
						break

			else:
				# construct header
				resp = version + " 404 Not Found\r\n\r\n"
				# send header
				error = clientSocket.sendall(resp.encode("utf-8"))

				if error is not None:
					print("Server: Error on sending 404 Not Found")
					break

				# open and send file
				with open(errorFile, 'rb') as f:
					error = clientSocket.sendall(f.read(bufferSize))

					if error is not None:
						print("Server: Error on sending error page")
						break

					endOfFile = "\r\n"
					error = clientSocket.sendall(endOfFile.encode("utf-8"))

					if error is not None:
						print("Server: Error on sending end of page")
						break

		print("Connection closed")
