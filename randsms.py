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

# write to log file
f = open('MessageRevievedFile.csv', 'a')
string = "%s, %s\n" %(form.getvalue("from"), form.getvalue("content"))
f.write(string)
f.close();

# Get the content from the string
stringNum = form.getvalue("content")

# Can we tokenise the string?
isList = re.search('^.*(,|\n|\r).*$', stringNum)
if isList:
	# Select a random list element
	listTokens = re.split(',|\n|\r', stringNum)
	selIdx = random.randrange(len(listTokens))
	textContent = listTokens[selIdx]
else:
	if str.isdigit(stringNum):
		# Pick a random list element
		textContent = random.randrange(int(stringNum))
	else:
		textContent = 'Input parse error'

# send response
message = clockwork.SMS(
	to = form.getvalue("from"),
	message = textNumber,
	from_name = 'RandSMS')

response = api.send(message)

# produce response
if response.success:
	print "HTTP/1.1 200 OK"
else:
	print "HTTP/1.1 500 Internal Server Error"
