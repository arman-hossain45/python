num=int(input("enter a mumber"))

if num%100==0:
    if num%400==0:
        print(num,"this year is leap year")
    
    else:
        print("not leap year")
elif num%4==0:
    print(num,"is  leap year")
else :
    print(num ,"is not leap year")
          