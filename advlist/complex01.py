#!/usr/bin/env python3

#!/usr/bin/env python3

# create a list called list1
list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]
list2 = ["juniper"]
list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]
# display list1
print(list1)  #this just printed list1

print(list1[1]) #this printed list one and the 01 of list one

list1.extend(list2)
print(list1)

list1.append(list3)
print(list1) 

# display the list of IP addresses
print(list1[4])

 # display the first item in the list (0th item) - first IP address
print(list1[4][0])
