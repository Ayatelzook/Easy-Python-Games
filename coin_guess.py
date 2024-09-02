import random
print("Welcome to the coin guessing game 😊😊")
print("choose the method to toss the coin :")
print("1.using random.random()")
print("2.using random.randint()")
choice=int(input("Enter your choice (1 or 2): "))
if choice==1:
    guess=random.random()
    your_guess=input("Enter your guess (Heads or Tails): ")
    if guess>0.5 and your_guess.lower()=="tails" or guess<0.5 and your_guess.lower()=="heads":
        print("congratulations ! 🎉🎉 You won")
        print (f"the computer's coin toss result : {guess} ")
    else:
        print("Sorry , You lost ")
        print (f"the computer's coin toss result : {guess} ")
elif choice==2:
    guess=random.randint(0,1)
    your_guess=input("Enter your guess (Heads or Tails): ")
    if guess==1 and your_guess.lower()=="tails" or guess==0 and your_guess.lower()=="heads":
        print("congratulations ! 🎉🎉 You won")
        print (f"the computer's coin toss result : {guess} ")
    else:
        print("Sorry , You lost ")
        print (f"the computer's coin toss result : {guess} ")
else:
    print("please enter correct choice (1 or 2 )")