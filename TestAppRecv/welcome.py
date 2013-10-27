#!/usr/bin/env python

import cgi
import random
form = cgi.FieldStorage()
print "Content-Type: text/html"
number = int(form.getvalue("number"))+1

print
print """\
<html>
<body>
<h2>Hello World!</h2>
"""
print "The user entered %s" % random.randrange(number)
print """\
</body>
</html>
"""



