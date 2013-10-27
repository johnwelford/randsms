#!/usr/bin/env python
# libraries and input setup
import cgitb
cgitb.enable()
import cgi
form = cgi.FieldStorage()
import random
import sys
#sys.path.append('../utils/lxml-3.2.3/src')
#sys.path.append('../utils/clockwork')
import clockwork
api = clockwork.API('f28dbd49244e960260e9a5d40de3411fb635ac5d')

# write to log file
f = open('MessageRevievedFile.csv', 'a')
string = "%s, %s\n" %(form.getvalue("from"), form.getvalue("content"))
f.write(string)
f.close();

# randomise
number = random.randrange(int(float(form.getvalue("number"))))

# send response
message = clockwork.SMS(
    to = form.getvalue("from"),
    message = number,
    from_name = 'RandSMS')

response = api.send(message)

# produce response
if response.success:
    print "HTTP/1.1 200 OK"
else:
    print "HTTP/1.1 500 Internal Server Error"

