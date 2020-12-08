#!/usr/bin/env python3
list = [ "10.10.10.10", 5060, "up" ]

print("the first item in the list: " + list[0])

print("the second item in the list: " + str(list[1]) )

print("the third item in the list: " + list[2] )

new_list = [5060, "80", "10.10.10.1", "10.20.20.20", "ssh"] 

print("When I ssh into IP addresses: " +new_list[2], " I am unable to ping ports: " + str(new_list[1]) ) 


