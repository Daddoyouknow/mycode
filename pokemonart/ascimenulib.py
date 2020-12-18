#!/usr/bin/env python3
from os import system #this is for the clear command

art = [{"name": "Bulbasaur", "ascii": "bulbasaur.ascii"}, {"name": "Charizard", "ascii": "charizard.ascii"}, {"name": "Charmander", "ascii": "charmander.ascii"}, {"name": "Charmeleon", "ascii": "charmeleon.ascii"},
        {"name": "Pikachu", "ascii": "pikachu.ascii"}, {"name": "Squirtle", "ascii": "squirtle.ascii"}, 
        {"name": "Quit", "ascii": "pokeball.ascii"}] 

system("clear")
title = open("pokemontitle.ascii")
print(title.read())
print("Welcome to Pokemon Print!!""\n")
print("---------------------------------------------------------------\n")    
title.close
while True:
    for ind, pokemon in enumerate(art):
        print(f"{ind}. {pokemon['name']}")
    choice = int(input("Enter the number of the pokemon you would like to see: "))
    o = open(art[choice]["ascii"])
    asci = o.read()
    if choice < 6:
        system("clear")
        print(art[choice]["name"] + " I CHOOSE YOU!!!\n ")
        print(asci)
    elif choice == 6:
        system("clear")
        print(asci)
        print("\nThank you for coming!!! Gotta Catch 'EM All!!!")
        quit( 
                )
   # else:
     #   print("sorry thats not a valid choice. Try again...\n")    

#while True:
   # ui = choice
   # try: 
    #    num = int(choice)
     #   break
   # except ValueError as err:
    #    print("sorry thats not a valid choice. Try again...\n")
     #   continue


   # elif choice > 6:
     #   print("sorry thats not a valid choice. Try again...\n")
#if choice == "6":
 #   print("Thank you for coming!!! Gotta Catch 'EM All!!!")    
  #  break

