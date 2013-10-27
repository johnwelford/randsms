#!/usr/bin/env python

import os
import cgi
form = cgi.FieldStorage()
print "Content-Type: text/html"


print
print """\
<html>
<body>
<h2>Hello World!</h2>
"""
print "The user entered %s" % os.getcwd()
print """\
</body>
</html>
"""



