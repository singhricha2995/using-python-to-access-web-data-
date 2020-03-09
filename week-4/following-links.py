#Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Mhurain.html
#Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
#Hint: The first character of the name of the last page that you will load is: U


import urllib.request
from bs4 import BeautifulSoup
import ssl
url=input("Enter the URL:")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count=int(input("Enter the count:"))
position=int(input("Enter the position:"))
for link in range(count):
    html=urllib.request.urlopen(url).read()
    soup=BeautifulSoup(html)
    
    tags=soup('a')
    x=[]
    y=[]
    for tag in tags:
        a=tag.get('href',None)
        x.append(a)
        b=tag.text
        y.append(b)
    print(x[position-1])
    print(y[position-1])
    url=x[position-1]
        
