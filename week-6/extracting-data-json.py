#
he program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

import urllib.request, urllib.parse, urllib.error
import json
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
sum=0
url=input('Enter url:')
uh=urllib.request.urlopen(url)
data=uh.read()
info=json.loads(data)
for items in info['comments']:
    count=int(items['count'])
    sum=sum+count
print(sum)
    
