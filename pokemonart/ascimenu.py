#!/usr/bin/env python3

#first we will diplay our pokemon title
title = open("pokemontitle.ascii")
print(title.read()) 
print("Welcome to Pokemon Print!!""\n")
#time.sleep(3)

#our user input

print( "1.bulbasaur  2.charizard 3.charmander 4.charmeleon 5.pikachu 6.squirtle""\n" )
choice = input( "which Pokemon would you like to see? choose a number:" )
#print( "you would like to learn more about:" + choice) 

#this is our variables for pokemon images to choose from 
bulb = open("bulbasaur.ascii")
zard = open("charizard.ascii")
mander = open("charmander.ascii")
meleon = open("charmeleon.ascii")
pika = open("pikachu.ascii")
squirt = open("squirtle.ascii")

#trying to make a while loop that will take the user back to the initial question if the input >7
while choice > "6":
   #print(input( "which Pokemon would you like to see? choose a number:" )
    print( "1.bulbasaur  2.charizard 3.charmander 4.charmeleon 5.pikachu 6.squirtle""\n" )
    choice = input( "Sorry?!? that wasn't an option. Please choose a number from above :" )
#print( "you would like to learn more about:" + choice) 

#this is our loop for display
if choice == "1":
    print("here is an image of bulbasaur")
    print(bulb.read())
elif choice == "2":
    print("here is an image of charizard")
    print(zard.read())
elif choice == "3":
    print("here is an image of charmander")
    print(mander.read())
elif choice == "4":
    print("here is an image of charmeleon")
    print(meleon.read())
elif choice == "5":
    print("here is an image of pikachu")
    print(pika.read())
elif choice == "6":
    print("here is an image of squirtle")
    print(squirt.read())
#else:                 # if answer was outside of choice range
       # print('Sorry. Try again!')

#print( "you would like to learn more about:" + choice) 
#list = [ "1.bulbasaur  2.charizard 3.charmander 4.charmeleon 4.pikachu 5.squirtle" ]

