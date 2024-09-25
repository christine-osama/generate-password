import random 
import string
print("welcome to password generator ")
characters=int(input("enter total number of character in password"))
letters=int (input("enter total number of letters in password"))
numbers=int (input("enter total number of numbers in password"))
symbols=int (input("enter total number of symbols in password"))
if characters!=(letters+numbers+symbols):
                           print("invalid input")
else:
                            password_chars=(random.choices(string.ascii_letters,k=letters)+random.choices(string.digits,k=numbers)+random.choices(string.punctuation,k=symbols))                              
random.shuffle(password_chars)
password="".join(password_chars)
print(password)          
