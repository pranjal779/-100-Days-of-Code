print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

travelToMissionBy = input(
    "How do you want to travel? by Land, by Air, or by Water: ")
if travelToMissionBy == "Land":
    print('''
                   .---._
           .--(. '  .).--.      . .-.
        . ( ' _) .)` (   .)-. ( ) '-'
       ( ,  ).        `(' . _)
     (')  _________      '-'
     ____[_________]                                         ________
     \__/ | _ \  ||    ,;,;,,                               [________]
     _][__|(")/__||  ,;;;;;;;;,   __________   __________   _| LILI |_
    /             | |____      | |          | |  ___     | |      ____|
   (| .--.    .--.| |     ___  | |   |  |   | |      ____| |____      |
   /|/ .. \~~/ .. \_|_.-.__.-._|_|_.-:__:-._|_|_.-.__.-._|_|_.-.__.-._|
+=/_|\ '' /~~\ '' /=+( o )( o )+==( o )( o )=+=( o )( o )+==( o )( o )=+=
='=='='--'==+='--'===+'-'=='-'==+=='-'+='-'===+='-'=='-'==+=='-'=+'-'jgs+

    ''')
    print("You will take 14 hours to reach your destination.")
elif travelToMissionBy == "Water":
    print('''
                       ~;
                  ,/|\,
                ,/' |\ \,
              ,/'   | |  \
            ,/'     | |   |
          ,/'       |/    |
        ,/__________|-----' ,
       ___.....-----''-----/
 jgs   \                  /
   ~~-~^~^~`~^~`~^^~^~-^~^~^~-~^~^
     ~-^~^-`~^~-^~^`^~^-^~^`^~^-~^
    ''')
    print("You will take 32 hours to reach your destination.")
elif travelToMissionBy == "Air":
    print('''
                                            |
                                      --====|====--
                                            |  
                                        .-"""""-. 
                                      .'_________'. 
                                     /_/_|__|__|_\_\
                                    ;'-._       _.-';
               ,--------------------|    `-. .-'    |--------------------,
                ``""--..__    ___   ;       '       ;   ___    __..--""``
                 jgs      `"-// \\.._\             /_..// \\-"`
                             \\_//    '._       _.'    \\_//
                              `"`        ``---``        `"`
    ''')
    print("You will take 10 hours to reach your destination.")
else:
    print("""You have no other option other than to travel by Road:
               .      ..
   __..---/______//-----.        ((  )
 .".--.```|    - /.--.  =:    ( VROOM! ))  
(.: {} :__L______: {} :__; __--( __- -_= ) 
   *--*           *--*                    
    """)
    print("With Car you will reach your destination in 16 hours.")


afterReachingDestination = input(
    "What local travel method you took?[Uber, lyft, taxi], Bus, Cycle, Car: ")
if afterReachingDestination == "Uber" or "lyft" or "taxi":
    print("The Treasure location is not in the Taxi APP, you came 3rd.")
elif afterReachingDestination == "Bus":
    print("Public Transport you were Lost, you came 2nd.")
elif afterReachingDestination == "Cycle":
    print("You took too long to arrive., you came 4th")
elif afterReachingDestination == "Car":
    print("You came in Car, you arrived 1st.")
else:
    print("Out of Scope.")

arrivedAtPosition = int(input("Arrival Position 1-4: "))
if arrivedAtPosition == 3:
    print("you did not get any part of the treasure, as you did not had the tools to dig the treasure.")
elif arrivedAtPosition == 2:
    print("You Slipped and fell into the pond.")
elif arrivedAtPosition == 4:
    print("Have the tools but still cycling to the location.")
elif arrivedAtPosition == 1:
    print("You got the Treasure, you had the tools, you arrived at the location the fastest.")
else:
    print("Out of Scope.")
