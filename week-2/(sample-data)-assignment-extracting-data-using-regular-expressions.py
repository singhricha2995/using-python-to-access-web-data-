The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

import re
name=input("Enter the filename:")
fn=open(name,'r')
count=0
total=0
for lines in fn:
    numbers=re.findall('[0-9]+',lines)
    for number in numbers:
        count=count+1
        total=total+int(number)
print(count)
print(total)
