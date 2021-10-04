"""
Password Generator

Password generator so that it also chooses from :-
small letters(a-z)
Capital letters (A-Z)
Numbers (0-9)
Punctuation (@,,$,&,*,!,%)

A passowrd is strong only if it consists of at least 8 characters and does not contain only letters.
"""

import random
str='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@$&*!%'  #Wide variety of characters as well as symbols to choose from to ensure a strong password.
pwd=''
leng=int(input('Enter length of password '))
for c in range(leng):  #leng denotes Length of password 
    pwd+=random.choice(str)  #loop iterates "leng" times.Each time a random character from the string "str" is chosen , till password contains "leng" characters.
print("Password generated is : "+pwd)
if leng<8:  
    print("Password strength : Weak") #Password strength is displayed accordingly.
else:
    print("Password strength : Strong") #Password strength is displayed accordingly.
