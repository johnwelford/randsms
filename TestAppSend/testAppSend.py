from clockwork import clockwork
 
api = clockwork.API('f28dbd49244e960260e9a5d40de3411fb635ac5d')
 
message = clockwork.SMS(
    to = '447814963513',
    message = 'Imagine a different random number.',
    from_name = 'AnIdiot')

 
response = api.send(message)
 
if response.success:
    print (response.id)
else:
    print (response.error_code)
    print (response.error_description)
