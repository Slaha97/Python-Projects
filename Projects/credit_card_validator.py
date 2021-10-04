"""
Credit Card Validator
The algorithm we're going to use to verify card numbers is called the Luhn algorithm, or Luhn formula.
The purpose of the algorithm is to identify potentially mistyped numbers, because it can determine whether or not it's possible 
for a given number to be the number for a valid card.

The way we're going to use the algorithm is as follows:

Remove the rightmost digit from the card number. This number is called the checking digit, and it will be excluded from most of our calculations.
Reverse the order of the remaining digits.
For this sequence of reversed digits, take the digits at each of the even indices (0, 2, 4, 6, etc.) and double them. If any of the results are greater than 9, subtract 9 from those numbers.
Add together all of the results and add the checking digit.
If the result is divisible by 10, the number is a valid card number. If it's not, the card number is not valid.
Let's look at this step by step for a valid number so we can see this in action. The number we're going to use is 5893804115457289, which is a valid Maestro card number, but not one which is in use.

Number	Operation
5893804115457289	       Starting number
589380411545728X	       Remove the last digit
827545114083985X	       Reverse the remaining digits
16214585218016318810X	   Double digits at even indices
725585218073981X	       Subtract 9 if over 9
Now we sum these digits and add the checking digit:

7 + 2 + 5 + 5 + 8 + 5 + 2 + 1 + 8 + 0 + 7 + 3 + 9 + 8 + 1 + 9

"""

print("WELCOME TO CREDIT CARD VALIDATOR")
print("--------------------------------")
n=input('Enter 16 digit card number : ')  #16 digit credit card no. is taken as input.Here input is taken as string. 
z=list(n)
u=int(z[-1])
p=z[:len(n)-1]
p.reverse()
j,k=[],[]
i,m,s=0,0,0
for i in range(len(p)):
    if i%2==0:
        j.append(int(p[i])*2)
    elif i%2==1:
        k.append(int(p[i]))
        
for m in range(len(j)):  
    if j[m]>9:
        j[m]=j[m]-9
        
s1=sum(j)
s2=sum(k)

if (s1+s2+u) %10==0:  #Condition of sum is checked here.The sum should be divisible by 10.
    print(n +" is a valid credit card number")
else:
    print(n +" is an invalid credit card number")


