print ("""
 @@@@@                                        @@@@@
@@@@@@@                                      @@@@@@@
@@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@
 @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@
     @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@
       @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@
         @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@
            @@@@@@@    @@@@@@    @@@@@@
            @@@@@@      @@@@      @@@@@
            @@@@@@      @@@@      @@@@@
             @@@@@@    @@@@@@    @@@@@
              @@@@@@@@@@@  @@@@@@@@@@
               @@@@@@@@@@  @@@@@@@@@
           @@   @@@@@@@@@@@@@@@@@   @@
           @@@@  @@@@ @ @ @ @ @@@@  @@@@
          @@@@@   @@@ @ @ @ @ @@@   @@@@@
        @@@@@      @@@@@@@@@@@@@      @@@@@
      @@@@          @@@@@@@@@@@          @@@@
   @@@@@              @@@@@@@              @@@@@
  @@@@@@@                                 @@@@@@@
   @@@@@                                   @@@@@
   """)
print("Welcome to my island")
print ("There are two doors in front of you . 🚪red door and 🚪blue door ")
input1=input("which door do you want to open ? ")
if input1.lower()=="red":
    print("Great! now you entered a room " )
    print("You found three boxes : 🎁 white ,🎁 black ,🎁 green ")
    input2=input("which box do you open ?")
    if input2.lower()=="white":
        print("oops! You opened a box filled with snakes  🐍🐍🐍🐍")
    elif input2.lower()=="black":
        print("oops! You opened a box filled with spiders 🕸️🕸️🕸️")
    elif input2.lower()=="green":
        print("congratulation! Yu found the treasure 💰💰💰")
    else:
        print ("Invalid choice 🤷‍♂️🤷‍♂️🤷‍♂️")
elif input1.lower()=="blue":
    print("oops! You chose the crocodile door 🐊🐊🐊")
    print("Game Over! ")
else:
    print("Invalid choice 🤷‍♂️🤷‍♂️🤷‍♂️")