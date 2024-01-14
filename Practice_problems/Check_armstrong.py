'''Check Armstrong
An Armstrong number is a number (with 'k' digits) 
such that the sum of its digits raised to 'kth' power is equal to the number itself. 
For example, 371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371. '''

n = int(input())
digits = len(str(n))
sum = 0
for i in str(n):
    sum = sum+(int(i)**digits)

if (n==sum):
    print("true")
else:
    print("false")