import random
'''for i in range(3, 16):
    if i % 3 == 0:
        print(i)
        #continue
       # break
       #pass
    else:
      #print(i)
      break
num=int(input("No of toffees that you wants:"))
av=10
i=1
while i<=num:
    if i<=av:
        print(i,"Collect your toffes")
    else:
        print("Not Available or Out of stock")
        break
    i=i+1
else:
    print("Thanks for Visiting,Again Visit")
'''
num=random.randint(50,90)
print(num)
count=1
while count<=5:
    a = int(input("Enter the Number between 50 and 90:"))
    if a==num:
        print("Right!You Win..")
        break
    else:
        count=count+1
else:
    print("You Loss ,Try again...")

