import random
words=["office","ayat","pointer","apple"]
random_word=random.choice(words)
length=len(random_word)
count_tries=0
result=[]
guesses=[]
print(length)
print("""
        +---+
            |
            |
            |
            |
            |""")
HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

for letter in random_word:    ##result=["_"]*len(random_word)
    result.append("_")
print (' '.join(result))

while "_" in result and count_tries<6 :
    guess=input("guess a letter ").lower()
    
    if guess in guesses:
        print ("You have already guessed that letter")
        count=6-count_tries
        print (f"you have {count} more tries")  
        continue
    else:
        guesses.append(guess)
    if guess not in random_word:
        count_tries+=1 
        print(HANGMAN[count_tries])
    for index in range(length):
        if random_word[index]==guess:
            result[index]=guess         
        
    print(' '.join(result))
    count=6-count_tries
    print (f"you have {count} more tries")      
    
    
if count_tries==6:
    print("""
          You lose
          """)    
    print ("""
             +---+
             |   |
             O   |
            /|\  |
            / \  |
                 |""")
    
else:   

    print (" **************** ")
    print ("    YOU WIN    ")
    print (" **************** ")
        
     