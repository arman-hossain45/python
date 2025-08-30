#print all multification 

n=int(input("enter a number which multipication table you want to see  = "))
sum=0
for i in range(1,11):
    print(i,"*",n,"=",i*n)
    sum=i*n
print(sum)


