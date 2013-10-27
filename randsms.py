#!/usr/bin/env python
# libraries and input setup
import sys
sys.path.append('../utils/lxml-3.2.3/src')
sys.path.append('../utils/clockwork')

import cgitb
import cgi
import random
import re
import clockwork

cgitb.enable()

api = clockwork.API('f28dbd49244e960260e9a5d40de3411fb635ac5d')
form = cgi.FieldStorage()

# Write to log file
f = open('MessageRevievedFile.csv', 'a')
string = "%s, %s\n" %(form.getvalue("from"), form.getvalue("content"))
f.write(string)
f.close();

# Get the content from the string
stringNum = form.getvalue("content")

# Can we tokenise the string?
listTokens = re.split(',|\n|\r', stringNum)
if len(listTokens)>1:
	# Select a random list element
	selIdx = random.randrange(len(listTokens))
	textContent = listTokens[selIdx]
else:
	if str.isdigit(stringNum):
		# Pick a random number in the specified range
		textContent = random.randrange(int(stringNum))
	else:
		textContent = "Message not understood. Please submit either a single positive integer or a list separated by commas or returns."

# Send text via Clockwork API response
message = clockwork.SMS(
	to = form.getvalue("from"),
	message = textContent,
	from_name = 'RandSMS')

response = api.send(message)

print "HTTP/1.1 200 OK"
