#!/usr/bin/env python3

proto = [ "ssh", "http", "https" ] 
print(proto)

print(proto[1])
proto.extend("dns") #this line will add d, n, and s This is a great method for combining two lists into a single list.
print(proto)

