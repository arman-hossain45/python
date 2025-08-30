a=int(input("enter a number"))
tax=0

if a>=10000:
    tax=15/100*a
    print(tax)
elif a>=5000 and a<10000:
    tax=10/100*a
    print(tax)
else:
    print("5% tax")