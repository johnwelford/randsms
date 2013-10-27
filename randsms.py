#!/usr/bin/env python
import cgitb
cgitb.enable()

import cgi
import random
form = cgi.FieldStorage()

import sys
sys.path.append('../utils/lxml-3.2.3/src')
sys.path.append('../utils/clockwork')

import clockwork

api = clockwork.API('f28dbd49244e960260e9a5d40de3411fb635ac5d')

f = open('MessageRevievedFile.csv', 'a')
string = "%s, %s\n" %(form.getvalue("from"), form.getvalue("content"))
f.write(string)
f.close();

number = random.randrange(int(form.getvalue("number")))


message = clockwork.SMS(
    to = form.getvalue("from"),
    message = number,
    from_name = 'RandSMS')

response = api.send(message)

if response.success:
    print "HTTP/1.1 200 OK"
else:
    print "HTTP/1.1 500 Internal Server Error"

