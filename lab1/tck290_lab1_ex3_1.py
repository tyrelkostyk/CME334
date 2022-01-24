"""
CME 334
Lab 1 - Exercise 3.1
Thursday Jan 20 2022

Tyrel Kostyk
tck290
11216033
"""

from urllib.request import urlopen

def get_image_names(website):
	""" Prints all .jpg filenames on a webpage. Assumes UTF-8 formatting. """

	filetype = ".jpg"

	# assume UTF-8 encoding
	encoding = "utf-8"

	# allow 10MB max download size
	max_size = 10 * 1024 * 1024

	# download and decode website data
	data = urlopen(website)
	data_decoded = data.read(max_size).decode(encoding)

	# extract image names
	index = 0
	image_names = []
	while True:
		# find next index of .jpg filename extension
		index = data_decoded.find(filetype, index)
		# stop searching if no further .jpg found
		if (index == -1): break
		# obtain the filename
		name_length = 0
		temp_index = index-1
		while (data_decoded[temp_index] not in ['"', "'"]):
			name_length += 1
			temp_index -= 1
		filename = data_decoded[index-name_length:index+len(filetype)]
		# save the filename
		image_names.append(filename)
		# increment index to find the next match
		index += 1


	# print out image names
	for name in image_names:
		print(name)
