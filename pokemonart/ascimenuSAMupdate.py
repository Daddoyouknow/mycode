#!/usr/bin/env python3
#------------>SAM, I have a few things I need help with. Feel free to comment  out below. 

#1.i need to be able to start the loop over from any choice. so if the user chose 1, the picture displays, i dont want it to leave the scipt. i would like for it to ask the "quit or more" question then got through the loop to choose another pokemon.

#2. when i press the number 10 in my choices it stops the script instead of asking for another option. i have a while loop at the bottom that says while choice > 6 it should ask to try again. this works as long as i dont go over 9.

#3. overall i will be adding more information and making it look nice but i want to be sure im greacefully entering and exiting the script. PLEASE ADD any suggestions<-------------------### 

#first we will define our pokemon title screen
def main():
    title = open("pokemontitle.ascii")
    print(title.read()) 
    print("Welcome to Pokemon Print!!""\n")
    print("---------------------------------------------------------------""\n")
    choice = input( "1.bulbasaur  2.charizard 3.charmander 4.charmeleon 5.pikachu 6.squirtle""\n"" which Pokemon would you like to see? choose a number:""\n""if you would like to Quit press q" )
    if choice == "q":
        break
    if choice == "1":
        print("here is an image of bulbasaur")
        print(bulb.read())
    #print( "you would like to learn more about:" + choice) 
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
leave()

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

