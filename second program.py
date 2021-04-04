import math as m
from datetime import date

'''celsius = float(input("Enter temperature celsius:"))
fahrenhiet = (celsius * 9 / 5) + 32
print('%.2f celsius=%0.2f fahrenhiet' % (celsius, fahrenhiet))

fahrenhiet = float(input("Enter Value in Fahrenhiet:"))
dc = (fahrenhiet - 32) * 5 / 9
print('%.2f fahrenhiet=%0.2f dc' % (fahrenhiet, dc))'''
fd = date(2021, 3, 28)
ld = date(2020, 2, 20)
day = fd - ld
print("Difference between dates=", day)

cal = eval(input("Enter Mathmetics expression:"))
print(cal)
