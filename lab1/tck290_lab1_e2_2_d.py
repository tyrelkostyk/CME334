"""
CME 334
Lab 1 - Exercise 2.2 (d)
Thursday Jan 20 2022

Tyrel Kostyk
tck290
11216033
"""

def print_subquote(input):
	""" Prints nested string within double quotes (minus the quotes). """

	# grab the index of the start of the substring
	startOfSubstring = input.find('"') + 1

	# grab the index of the end of the substring
	endOfSubstring = input.find('"', startOfSubstring)

	return input[startOfSubstring:endOfSubstring]
