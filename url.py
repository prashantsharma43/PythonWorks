import urllib2
from urllib2 import *
import json

url = 'http://google.com'

goog = urllib2.urlopen(url).read()

print goog
