#!/usr/bin/env python3


#Author: Genavous Bell 
#Summary: Pokemon ASCII Art Menu- The script demonstartes the ablitly to create a query system with a menu interface.
#Created: 12/22/2020

from os import system #this is for the clear command

#dictionary of Pokemon to choose from
art = [{"name": "Bulbasaur", "ascii": "bulbasaur.ascii"}, {"name": "Charizard", "ascii": "charizard.ascii"}, {"name": "Charmander", "ascii": "charmander.ascii"},
        {"name": "Charmeleon", "ascii": "charmeleon.ascii"},
        {"name": "Pikachu", "ascii": "pikachu.ascii"}, {"name": "Squirtle", "ascii": "squirtle.ascii"}, 
        {"name": "Eevee", "ascii": "evee.ascii"}, {"name": "Gloom", "ascii": "gloom.ascii"}, {"name": "Jigglypuff", "ascii": "jigglypuff.ascii"}, 
        {"name": "Kadabra", "ascii": "kadabra.ascii"}, {"name": "Machamp", "ascii": "machamp.ascii"}, {"name": "Mr.Mime", "ascii": "mrmime.ascii"},
        {"name": "Onix", "ascii": "onix.ascii"}, {"name": "Pidgeotto", "ascii": "pidgeotto.ascii"}, {"name": "Psyduck", "ascii": "psyduck.ascii"},
        {"name": "Raichu", "ascii": "raichu.ascii"}, {"name": "Rapidash", "ascii": "rapidash.ascii"}, {"name": "Abra", "ascii": "abra.ascii"},
        {"name": "Butterfree", "ascii": "butterfree.ascii"}, {"name": "Quit", "ascii": "pokeball.ascii"}]

#defining functions
def title(): 
    system("clear")
    title = open("pokemontitle.ascii")
    print(title.read())
    print("Welcome to Pokemon Print!!""\n")
    print("---------------------------------------------------------------\n")    
    title.close

def main():
    while True:
        for ind, pokemon in enumerate(art):
            print(f"{ind}. {pokemon['name']}",end= '  ')
        try:
            choice = int(input("\n\nEnter the number of the Pokemon you would like to see: "))
            o = open(art[choice]["ascii"])
            asci = o.read()
        except ValueError as err:
            system("clear")
            print("\nSorry.. That isn't an option.. Please try again---\_('_')_/--- \n")
            continue
        except IndexError as err:
            system("clear")
            print("\nSorry.. That isn't an option.. Please try again---\_('_')_/--- \n")
            continue
        if choice < 19:
            system("clear")
            print(art[choice]["name"] + " I CHOOSE YOU!!!\n ")
            print(asci)
        elif choice == 19:
            system("clear")
            print(asci)
            print("\nThank you for coming!!! Gotta Catch 'EM All!!!\n")
            quit()

#run it
title()
main()


