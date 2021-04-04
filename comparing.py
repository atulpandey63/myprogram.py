x = int(input("Enter first number:"))
y = int(input("Enter Second Number:"))
z = int(input("Enter third Number:"))

if x > y:
    if x > z:
        print("'X' is greatest Number ")
    else:
        print("'Z' is greatest Number")

elif y > z:
    print("'Y' is greatest number")
else:
    print("'Z' is greatest no")

if x == y == z:
    print("All three numbers are equal")
