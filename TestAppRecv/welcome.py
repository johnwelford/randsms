#!/usr/bin/env python
import cgitb
cgitb.enable()

import cgi
import random
form = cgi.FieldStorage()
#print "Content-Type: text/html"
# number = int(form.getvalue("number"))
>>>>>>> 469792c025d8f8aa5bcc6ff776059acc27535109

#print
#print """\
#<html>
#<body>
#<h2>Hello World!</h2>
#"""
#print "The user entered %s" % random.randrange(number)

f = open('MessageRevievedFile.csv', 'a')
string = "%s, %s\n" %(form.getvalue("from"), form.getvalue("content"))
f.write(string)
f.close();

print "HTTP/1.1 200 OK"
#print """\
#</body>
#</html>
#"""
#
#
#
