#!/usr/bin/env python
import sys
sys.path.append('./lxml-3.2.3/src')
import clockwork

#print "Content-Type: text/html"
#print
#print """\
#<html>
#<body>
#<h2>Hello World!</h2>
#</body>
#</html>
#"""
api = clockwork.API('f28dbd49244e960260e9a5d40de3411fb635ac5d')
 
message = clockwork.SMS(
    to = '447814963513',
    message = 'What number am I think of.',
    from_name = 'RandSMS')

 
response = api.send(message)
 
if response.success:
    print (response.id)
else:
    print (response.error_code)
    print (response.error_description)
