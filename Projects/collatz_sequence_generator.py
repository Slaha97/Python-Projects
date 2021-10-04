"""
Starting with any positive integer N, Collatz sequence is defined corresponding to n as the numbers formed by the following operations :
 

If n is even, then n = n / 2.
If n is odd, then n = 3*n + 1.
Repeat above steps, until it becomes 1

Examples : 

Input : 3
Output : 3, 10, 5, 16, 8, 4, 2, 1       

Input : 6
Output : 6, 3, 10, 5, 16, 8, 4, 2, 1

"""

print('WELCOME TO COLLATZ SEQUENCE GENERATOR')
print('-------------------------------------')
n=int(input('Enter the first term of the sequence : '))
print('The sequence goes as follows: \n')
while n>1:
    print(n)
    if n%2==0:
        n=int(n/2)
    else:
        n=int(3*n+1)
        
print(n)