a=int(input("enter a number"))

if a>0:
    if a%2==0:
        print(a,"is positive num and even num ")
    else:
        print(a,"is positive num and odd num")
elif a<0:
    if a%2==0:
        print(a,"is negative num and even num ") 
    else:
        print(a,"is negative number and odd num")
else:
    print("number is zero ")