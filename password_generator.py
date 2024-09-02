import random
import string
print("Welcome to the password generator ")
num=int(input("Enter the total number of characters in the password : "))
num_letters=int(input ("Enter the number of letters in the password : "))
num_numbers=int(input("Enter the number of numbers in the password : "))
num_symbols=int(input("Enter the number of symbols in the password : "))
password=[]

sum=num_letters+num_symbols+num_numbers
if sum!=num:
    print("invalid input! the sum of letters,numbers,symbols doesn't match the number of characters in password")
else:
    letters=random.choices(string.ascii_letters,k=num_letters)
    password.extend(letters)
    numbers=random.choices(string.digits,k=num_numbers)
    password.extend(numbers)
    symbols=random.choices(string.punctuation,k=num_symbols)
    password.extend(symbols)
    out=random.shuffle(password)    ##random.shuffle it will make the changes on password it self
    print("".join(password))
    
    
    
    