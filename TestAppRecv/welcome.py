#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()
print "Content-Type: text/html"


print
print """\
<html>
<body>
<h2>Hello World!</h2>
"""
print "The user entered %s" % form.getvalue("name")
print """\
</body>
</html>
"""



