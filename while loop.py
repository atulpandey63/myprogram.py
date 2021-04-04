x = int(input("Enter Number:"))
i = 1
fact = 1
# print("Table of ",x)
'''while i <= 10:
    y=x*i
    i = i + 1
    print(y)'''
while i <= x:
    fact = fact * i
    i = i + 1

print("Factorial no=", fact)
