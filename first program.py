'''print("This is my first python program")
x = input("Enter No:")
#print(type(x))
a = int(x)
print(type(a))
ch = input("Please Enter character:")
print(ch[0])'''
# import math as m
from math import sqrt, pow, factorial,fabs

a = int(input("Enter no to get square root:"))
b = int(input("Enter first no:"))
c = int(input("Enter second no:"))
x = sqrt(a)
# print(x)
y = pow(b, c)
print("Square root of This no=", x, "Power of this no=", y)
z = factorial(c)
q= fabs(c)
print("Fabs No =", q)
print("Factorial No =", z)
