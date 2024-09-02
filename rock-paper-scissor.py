import random

# Save Ascii in variables
rock = """
   _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
"""
paper = """
  _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
"""
scissor = """
 _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
"""
print("Welcome to the Rock, Paper, Scissors game:")
input1 = input("press enter to continue or type (Help) for the rules help ").lower()
if input1 == "help":
    print("""       
                    ***************Rules****************       
                    1) You choose and the computer chooses
                    2) Rock smashes scissors -> Rock wins
                    3) Scissors cut paper -> Scissors wins
                    4) Paper covers Rock -> Paper wins
                 """)
input2 = input("Enter your choice (rock,paper,scissor): ").lower()
if input2 not in ["rock", "scissor", "paper"]:
    print("invalid choice .please run the program again and choose (rock,paper,scissor) ")
else:
    if input2 == "rock":
        print(f"You chose \n{rock}")
    elif input2 == "paper":
        print(f"You chose \n{paper}")
    elif input2 == "scissor":
        print(f"You chose \n{scissor}")
    computer_choice = random.choice(["rock", "paper", "scissor"])
    if computer_choice == "rock":
        print(f"Computer chose \n{rock}")
    elif computer_choice == "paper":
        print(f"Computer chose \n{paper}")
    elif computer_choice == "scissor":
        print(f"Computer chose \n{scissor}")

    if computer_choice == input2:
        print("it is a tie")
    elif (input2 == "rock" and computer_choice == "paper") or (input2 == "paper" and computer_choice == "scissor") or (
            input2 == "scissor" and computer_choice == "rock"):
        print(f"You lose {computer_choice} beats {input2} ")
    else:
        print(f"congratulations!🎉🎉  You win {input2} beats {computer_choice}")

