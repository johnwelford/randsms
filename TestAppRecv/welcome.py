#!/usr/bin/env python
import cgitb
cgitb.enable()

import cgi
import random
form = cgi.FieldStorage()
#print "Content-Type: text/html"
number = int(form.getvalue("number"))

#print
#print """\
#<html>
#<body>
#<h2>Hello World!</h2>
#"""
#print "The user entered %s" % random.randrange(number)

f = open('MessageRevievedFile.csv', 'a')
string = "The user entered %s\n" % random.randrange(number)
f.write(string)
f.close();

#print """\
#</body>
#</html>
#"""
#
#
#
