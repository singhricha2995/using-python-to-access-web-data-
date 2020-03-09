#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
#Actual data: http://py4e-data.dr-chuck.net/comments_366328.xml (Sum ends with 99)


import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter url:')
data=urllib.request.urlopen(url).read()
sum=0
tree=ET.fromstring(data)
lst=tree.findall('.//count')
for items in lst:
    count=items.text
    count=int(count)
    sum=sum+count
print(sum)
    
