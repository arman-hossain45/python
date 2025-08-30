a=int(input("enter a number = "))

if a<=100 and a>=90:
    print("you got a+")
elif a>=80 and a<90:
    print("you got a ")
elif a<80 and a>=70:
    print("you got A-")
elif a<70 and a>=60:
    print("tou got B ")
else:
    print("fail")