#!/usr/bin/env python3
# create the list called vendors
vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]
# loop across the list vendors
approved_vendors = ["cisco", "juniper", "big_ip"]
for x in vendors:
    print("The vendor is:" + x, end="" ) # newline, print current vendor, and end without newline
    if x not in approved_vendors:   # if x does not appear within the list approved_vendors
        print(" - NOT AN APPROVED VENDOR!", end="")
print("\nOur loop has ended.")  # when the loop ends print this

