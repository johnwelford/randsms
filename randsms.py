#!/usr/bin/env python
import cgitb
cgitb.enable()

import cgi
import random
form = cgi.FieldStorage()

import sys
sys.path.append('../../utils/lxml-3.2.3/src')
sys.path.append('../../utils/clockwork')

import clockwork

api = clockwork.API('f28dbd49244e960260e9a5d40de3411fb635ac5d')


# number = int(form.getvalue("number"))
f = open('MessageRevievedFile.csv', 'a')
string = "%s, %s\n" %(form.getvalue("from"), form.getvalue("content"))
f.write(string)
f.close();

print "HTTP/1.1 200 OK"

#print "The user entered %s" % random.randrange(number)


message = clockwork.SMS(
    to = form.getvalue("from"),
    message = form.getvalue("content"),
    from_name = 'RandSMS')

response = api.send(message)

if response.success:
    print (response.id)
else:
    print (response.error_code)
    print (response.error_description)
