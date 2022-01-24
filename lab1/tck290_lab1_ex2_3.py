"""
CME 334
Lab 1 - Exercise 2.3
Thursday Jan 20 2022

Tyrel Kostyk
tck290
11216033
"""

def use_NSID(line):
	fields = line.split(",")
	return fields[0]

def print_records(filename):
	""" Prints student grade records to stdout"""

	file = open(filename, "r")

	sorted_records = []

	for line in file:
		# place the line in a List
		sorted_records.append(line)

	# sort the list based on NSID (descending)
	sorted_records.sort(key=use_NSID)

	# print out the sorted records
	for line in sorted_records:
		fields = line.split(",")
		# ignore any records that don't have exactly 3 fields
		if (len(fields) < 3):
			return
		print(fields[0], fields[1], fields[2])

	file.close()
