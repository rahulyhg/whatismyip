import sys
import urllib2 
from lxml import html
url="http://dataindi.com/whatismyip.php"
sock = urllib2.urlopen(url)
htmlSource = sock.read()
sock.close()
print "\n....YOU IP IS.....\n"
print htmlSource
print "\n";