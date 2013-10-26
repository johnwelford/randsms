#!/usr/bin/env python
import sys
sys.path.append('../../utils/lxml-3.2.3/src')
sys.path.append('../../utils/clockwork')

import clockwork

api = clockwork.API('f28dbd49244e960260e9a5d40de3411fb635ac5d')
 
message = clockwork.SMS(
    to = '447814963513',
    message = 'What number am I think of.',
    from_name = 'RandSMS')

 
# response = api.send(message)
response = 1
 
if response.success:
    print (response.id)
else:
    print (response.error_code)
    print (response.error_description)
