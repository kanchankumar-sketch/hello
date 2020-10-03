print("hello")
#How to swap 2 variable with the help of 3rd  variable .
a=int(input("Enter value of first variable: "))
b=int(input("Enter value of second variable: "))
C=a
a=b
b=C
print("a is :",a," b is :",b)

#How to swap 2 variable without the help of 3rd  variable .
a=int(input("Enter value of first variable: "))
b=int(input("Enter value of second variable: "))
a=a+b
b=a-b
a=a-b
print("a is :",a," b is :",b)


#How to swap 3 variable without help of 4th variable.

a = int(input())
b = int(input())
c = int(input())
a = a + b + c
b = a - b-c
c = a - b-c
a = a - b-c
print("After swapping a = ",a,", b = ",b,", c = ",c) 


# Find the factorial of a number
n=int(input()) 
fact=1 
while n>0: 
fact=fact*n 
n=n-1 
print(fact) 

#Check whether a number is Perfect number or not

n=int(input()) 
i=1 
while i<=n/2: 
  if n%i==0: 
   sum+=i 
  i=i+1 
if sum==n: 
  print("Yes") 
else: 
  print("No") 
  
  #Check whether number is prime or not. 
  
  n=int(input()) 
if n<=1: 
  print("Not Prime") 
else: 
  flag=0 
  for i in range(2,n//2+1): 
   if n%i==0: 
    print("Not Prime") 
    flag=1 
    break 
  if flag==0: 
   print("Prime") 
