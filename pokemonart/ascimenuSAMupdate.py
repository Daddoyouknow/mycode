#!/usr/bin/env python3

#at least 5 more images..1 being a good bye image
#look into sounds
#loading animation
#make reading files variables
#take a look at screenshots to see if we can use dictionaries instead


import time
from os import system
#first we will define our pokemon title screen
def main():
    title = open("pokemontitle.ascii")
    print(title.read()) 
    print("Welcome to Pokemon Print!!""\n")
    print("---------------------------------------------------------------""\n")
    while True:    
        choice = input( "1.bulbasaur  2.charizard 3.charmander 4.charmeleon 5.pikachu 6.squirtle\n\nChoose the number of the Pokemon you would like to see or enter q to quit:")
        if choice == "1":
            system("clear")
            print("Bulbasaur I Choose YOU!!")
            print(bulb.read())
        elif choice == "2":
            system("clear")
            print("Charizard I Choose YOU!!")
            print(zard.read())
        elif choice == "3":
            system("clear")
            print("Charmander I Choose YOU!!")
            print(mander.read())
        elif choice == "4":
            system("clear")
            print("Charemeleon I Choose YOU!!")
            print(meleon.read())
        elif choice == "5":
            system("clear")
            print("Pikachu I Choose YOU!!")
            print(pika.read())
        elif choice == "6":
            system("clear")
            print("Squirtle I Choose YOU!!")
            print(squirt.read())
        elif choice == "q":
            system("clear")
            #time.sleep(3)
            print("\nPlease come again!!! Catch 'em All!!!") 
            break
        else:
            print("\nSorry that wasn't an option. Please try again...\n ")



#art = [{ "name1": "bulbasaur","ascii": "bulbasaur.ascii", "name2": "charizard", "ascii": "charizard.ascii"}] 

#3.charmander 4.charmeleon 4.pikachu 5.squirtle" ]


#this is our variables for pokemon images to choose from 
bulb = open("bulbasaur.ascii")
zard = open("charizard.ascii")
mander = open("charmander.ascii")
meleon = open("charmeleon.ascii")
pika = open("pikachu.ascii")
squirt = open("squirtle.ascii")

main() 

#trying to make a while loop that will take the user back to the initial question if the input >7
#this is our loop for display

#while choice > "6":
   #print(input( "which Pokemon would you like to see? choose a number:" )
#    print( "1.bulbasaur  2.charizard 3.charmander 4.charmeleon 5.pikachu 6.squirtle""\n" )
 #   choice = input( "Sorry?!? that wasn't an option. Please choose a number from above :" )

#exit = input("if you would like to quit press q if you would like to see more press m: ")
#if exit == "q":
   # print("thank you for coming. Bye!!")
    #break 
    

#lets diplay the title 
#print( "you would like to learn more about:" + choice)
#I want to make it so if the choice is in range it gives more options
   #print(input( "which Pokemon would you like to see? choose a number:" )
    
#print( "you would like to learn more about:" + choice)



#else:                 # if answer was outside of choice range
       # print('Sorry. Try again!')

#print( "you would like to learn more about:" + choice) 
#list = [ "1.bulbasaur  2.charizard 3.charmander 4.charmeleon 4.pikachu 5.squirtle" ]

