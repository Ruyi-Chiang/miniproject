import os
import urllib

file_path = os.getcwd() + "/movie_quotes.txt"


def read_text():
	quotes = open(file_path)
	contents = quotes.read()
	print contents
	quotes.close()
	check_profanity(contents)

def check_profanity(word_to_check):
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + word_to_check)
	output = connection.read()
	connection.close()
	if "true" in output:
		print "Profanity alert!!"
	elif "false" in output:
		print "This document has no curse words."


read_text()