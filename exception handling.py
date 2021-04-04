
'''if y == 0:
    print("Division is not possible due to denominator is zero")
else:
    div = x / y
    print("Value of Division=", div)
    print("Thank you")'''
try:
    print("Freez is OPEN")
    x = int(input("Enter the First Number:"))
    y = int(input("Enter the second Number:"))
    div = x / y
    print("Value of Division=", div)
    print("Thank you")

except ZeroDivisionError:
    print("Division is not possible due to denominator is zero")

except ValueError:
    print("The value you are entered is Invalid")

except Exception:
    print("Somethings went wrong...")

finally:
    print("Freez is CLOSED")
    print("Thank You")