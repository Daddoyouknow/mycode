#!/usr/bin/env python3
import urllib.request
import re
print("Where should we search?")
print("Great! So we'll try to open this url " + str(url) + " to search for the phrase:")

url = "https://alta3.com"
searchFor = input(alta3 )
searchMe = urllib.request.urlopen(url).read().decode("utf-8")
if re.search(searchFor, searchMe):
    print("Found a match!")
else:
    print("No match!")

