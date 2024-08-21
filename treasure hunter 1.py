print("Welcome to the Island of treasures")
#ascii arts you get pictures
print('''
    ___ __ 
   (_  ( . ) )__                  '.    \   :   /    .'
     '(___(_____)      __           '.   \  :  /   .'
                     /. _\            '.  \ : /  .'
                .--.|/_/__      -----____   _  _____-----
_______________''.--o/___  \_______________(_)___________
       ~        /.'o|_o  '.|  ~                   ~   ~
  ~            |/    |_|  ~'         ~
               '  ~  |_|        ~       ~     ~     ~
      ~    ~          |_|O  ~                       ~
             ~     ___|_||_____     ~       ~    ~
   ~    ~      .'':. .|_|A:. ..::''.
             /:.  .:::|_|.\ .:.  :.:\   ~
  ~         :..:. .:. .::..:  .:  ..:.       ~   ~    ~
             \.: .:  :. .: ..:: ./
    ~      ~      ~    ~    ~         ~
               ~           ~    ~   ~             ~
        ~         ~            ~   ~                 ~
   ~                  ~    ~ ~                 ~
''')
print("Welcome to the Island of treasures")
print("Here is your treasure but there are many consequences ")
user = input(" Are you brave to face the consequences ? yes or no\n").lower()
if user =="yes":
    print("""
     ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
    """)
    print(" Now you are into the game ................")
    choice1 = input('YOU\'RE AT THE STARTING POINT , CHOOSE "left" OR "right"\n').lower()
    if choice1 == "right":
          choice2 = input('Wow you choice the right option,Now you are at the museum . '
                       'Do you want to "move on" or "get into"'
                          '(type one of the  option) \n').lower()
          if choice2 == "move on":

                print("""
                            ,  O
                }\   o
      )    \  .'  `\ .
     (     }}<   ( 6>   )
    ) )    /  `,  .'   (   (
   ( (          }/      )   )
    ) )         '      (   (
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                """)
                choice3 = input('Now you are nearby a river, '
                                'do you like to  "wait" a boat or need to "walk"? \n ').lower()
                if choice3== "walk":
                    print(" Your choice was cool , "
                          "in 3 minutes you will reach the other side ")
                    print("There is a House after walk for a minute ,"
                          " Enter into that House  ")

                    print("""
                                __________
           |  __  __  |       __________
           |  __  __  |                           
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________|      __________
                 """)
                    choice4 = input('There are 3 doors , "A","B" and "C". '
                                    'Which one you choose?').upper()
                    if choice4 =="A":
                        print("You found your Treasure....CONGRAGULATIONS !")
                    else:
                        print("NO MORE LIFE, GAME OVER")
                else:
                    print("There is no boat ,you lose !\n"
                          " GAME OVER ")


          else:
               print(" The diano in the museum attached you,\n GAME OVER ")

    else:
        print("No more steps , you lost ")



