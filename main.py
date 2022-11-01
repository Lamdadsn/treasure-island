# Treasure island - choose your own adventure game
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
import os
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print('''
                  __..-----')
        ,.--._ .-'_..--...-'
       '-"'. _/_ /  ..--''""'-.
       _.--""...:._:(_ ..:"::. \
       
    .-' ..::--""_(##)#)"':. \ \)    \ _|_ /
   /_:-:'/  :__(##)##)    ): )   '-./'   '\.-'
   "  / |  :' :/""\///)  /:.'    --(       )--
     / :( :( :(   (#//)  "       .-'\.___./'-.
    / :/|\ :\_:\   \#//\            /  |  \
    
    |:/ | ""--':\   (#//)              '
    \/  \ :|  \ :\  (#//)
         \:\   '.':. \#//\
         
          ':|    "--'(#///)
                     (#///)         ___/""\     
                      \#///\           oo##
                      (##///)         `-6 #
                      (##///)          ,'`.
                      (##///)         // `.\
                      
                      (##///)        ||o   \\
                       \##///\        \-+--//
                       (###///)       :_|_(/
                       (sjw////)__...--:: :...__
                       (#/::""""        :: :     ""--.._
                  __..-"" ""          __;: :            "-._
          __..--""                  `---/ ;                '._
 ___..--""                             `-'                    "-..___
   (_ ""---....___                                     __...--"" _)
     """--...  ___"""""-----......._______......----"""     --"""
                   """"       ---.....   ___....----
 
''')
print("... You are shipwrecked on a tropical island...\n")
print("Sandy beaches lie to your left and right. Tropical jungle lies ahead.") 
choice = input("Which way do you want to go? L=Left, R=Right, A=Straight Ahead\n") 
lc_choice = choice.lower()
os.system('clear')
result = "?"
final_choice = "?"
if lc_choice == "r" or lc_choice == "right":
  print("\nA great wave sweeps up onto the score and drags you out to sea to a hungry shark.")
  print('''
                                     ,-
                                 ,'::|
                                /::::|
                              ,'::::o\                                      _..
           ____........-------,..::?88b                                  ,-' /
   _.--"""". . . .      .   .  .  .  ""`-._                           ,-' .;'
  <. - :::::o......  ...   . . .. . .  .  .""--._                  ,-'. .;'
   `-._  ` `":`:`:`::||||:::::::::::::::::.:. .  ""--._ ,'|     ,-'.  .;'
       """_=--       //'doo.. ````:`:`::::::::::.:.:.:. .`-`._-'.   .;'
           ""--.__     P(       \               ` ``:`:``:::: .   .;'
                  "\""--.:-.     `.                             .:/
                    \. /    `-._   `.""-----.,-..::(--"".\""`.  `:\
                    
                     `P         `-._ \          `-:\          `. `:\
                     
                                     ""            "            `-._)
  ''')
  print("\nBetter luck next time! :-(")
  result = "d"
elif lc_choice == "l" or lc_choice == "left":    # along the beach to a cave
  print("At the end of the beach there is a cliff with a cave.")
  print('''
 ********************************************************************************
*                    /   \              /'\       _                              *
*\_..           /'.,/     \_         .,'   \     / \_                            *
*    \         /            \      _/       \_  /    \     _                     *
*     \__,.   /              \    /           \/.,   _|  _/ \                    *
*          \_/                \  /',.,''\      \_ \_/  \/    \                   *
*                           _  \/   /    ',../',.\    _/      \                  *
*             /           _/m\  \  /    |         \  /.,/'\   _\                 *
*           _/           /MMmm\  \_     |          \/      \_/  \                *
*          /      \     |MMMMmm|   \__   \          \_       \   \_              *
*                  \   /MMMMMMm|      \   \           \       \    \             *
*                   \  |MMMMMMmm\      \___            \_      \_   \            *
*                    \|MMMMMMMMmm|____.'  /\_            \       \   \_          *
*                    /'.,___________...,,'   \            \   \        \         *
 ********************************************************************************
  ''')
  choice = input("Do you climb the cliff or enter the cave? C=Climb, E=Enter\n") 
  lc_choice = choice.lower()
  if lc_choice == "c":
      print("You fell and died")
      result = "d"
  else:
      os.system('clear')
      print("You found a shortcut. The cave opens out into a clearing with 3 doors.")
      final_choice = "d"
else: #lc_choice == "a" or lc_choice == "straight ahead" ... straight ahead to the jungle river
  print("You head straight into the jungle and come to a river.")
  print("In the distance you can see a skeleton rowing a boat toward you.")
  choice = input("Do you wait for the boat or dive in and swim? W=Wait, S=Swim\n") 
  lc_choice = choice.lower()
  if lc_choice == "s":
      print("You don't get very far before the water starts to bubble ... too late you realise that there are pirahnas in the water.")
      result = "d"
  else:
      os.system('clear')
      print("The skeleton is friendly. He takes you to a clearing on the other side of the river. There are 3 doors.")
      final_choice = "d"
# Choose which door
if final_choice == "d":
  print ('''
            __________       __________         __________
           |  __  __  |     |  __  __  |       |  __  __  |
           | |  ||  | |     | |  ||  | |       | |  ||  | |
           | |  ||  | |     | |  ||  | |       | |  ||  | |
           | |__||__| |     | |__||__| |       | |__||__| |
           | |__||_() |     | |__||_() |       | |__||_() |
           | |  ||  | |     | |  ||  | |       | |  ||  | |
           | |  ||  | |     | |  ||  | |       | |  ||  | |
           | |  ||  | |     | |  ||  | |       | |  ||  | |
           | |  ||  | |     | |  ||  | |       | |  ||  | |
           | |__||__| |     | |  ||  | |       | |  ||  | |
           |__________|     |__________|       |__________|
  ''')
  print ("Each door is a different colour.")
  print ("The left-most door is Red. The middle door is Yellow. The right-most door is Blue.")
  choice = input("Which door do you choose? R=Red, Y=Yellow, B=Blue\n")
  os.system('clear')
  print("You step though ...")
  lc_choice = choice.lower()
  if lc_choice == "r":
      print("Instantly you are engulfed by flames!")
      result = "d"
  elif lc_choice == "b":
      print("The last thing you ever see is claws reaching for you from out of the darkness!")
      print('''
                                             ,--,  ,.-.
                ,                   \,       '-,-`,'-.' | ._
               /|           \    ,   |\         }  )/  / `-,',
               [ '          |\  /|   | |        /  \|  |/`  ,`
               | |       ,.`  `,` `, | |  _,...(   (      _',
               \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L\
               
                \  \_\,``,   ` , ,  /  |         )         _,/
                 \  '  `  ,_ _`_,-,<._.<        /         /
                  ', `>.,`  `  `   ,., |_      |         /
                    \/`  `,   `   ,`  | /__,.-`    _,   `\
                    
                -,-..\  _  \  `  /  ,  / `._) _,-\`       \
                
                 \_,,.) /\    ` /  / ) (-,, ``    ,        |
                 
                ,` )  | \_\       '-`  |  `(               \
                
               /  /```(   , --, ,' \   |`<`    ,            |
              /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
        ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
       (-, \           ) \ ('_.-._)/ /,`    /
       | /  `          `/ \\ V   V, /`     /
    ,--\(        ,     <_/`\\     ||      /
   (   ,``-     \/|         \-A.A-`|     /
  ,>,_ )_,..(    )\          -,,_-`  _--`
 (_ \|`   _,/_  /  \_            ,--`
  \( `   <.,../`     `-.._   _,-`
   `                      ```      
      ''')
      result = "d"
  else:
      result = "t"
      print("A golden light bursts forth and when it fades away you see before you ...")
      print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
      ''')

if result == "d":
  print('''
                   __
                 (    )
                 __)(__
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          |  oooo oooo oooo  ||
          |                  ||
  *       | *   **    * **   |**      **
   \))ejm97/.,(//,,..,,\||(,,.,\\,.((//
   ''')

