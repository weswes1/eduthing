import re

thefile = open('bigarray.txt','r')

aPattern = re.compile("[a-z| ]")

thing = aPattern.findall(thefile.read())
thing = ''.join(thing)
thing = thing.split(" ")
print(thing[0])


