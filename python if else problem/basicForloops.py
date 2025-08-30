# name="arman"

# for i in name:
#     print(i)
#     if i=="a":
#         print("baby")



# colour=["red","blue","green","orange"]

# for colours in colour:
#     print(colours)
#     for i in colours:
#         print(i)

#print all even number between 1 to 50 

#n=int(input("enter a number"))
#for i in range(2,n+1,2):
      # print(i)


#print all square between 1 to 10 


###n=int(input("enter a number please = "))

#for i in range(1,n+1):
   # print(i*i)



#print all the element in given list
"""
list=["red","orange","green"]
for i in list:
    print(i)
    for j in i:
        print(j)



n=str(input("enter a string =  "))
for i in n:
    print(i)


# sum 1 to 100 number 

n=100

sum=0
for i in range(1,n+1):
    sum=sum+i
    print (sum)



#multipication table in python programming language 

n=int(input("enter a number which multipication table you want to see  = "))

for i in range(1,11):
    print(i,"*",n,"=",i*n)


#print all multification 

n=int(input("enter a number which multipication table you want to see  = "))
sum=0
for i in range(1,11):
    print(i,"*",n,"=",i*n)
    sum=i*n
print(sum)



n=str(input("enter a string = "))

count=0

vowel="aeiou"
for i in n:
    if i in vowel:
        count=count+1
print ("number of vowel in this string= ",count)



n=int(input("enter a number = "))

for i in range(1,n+1):
    if i%2==0:
        print(i,"is a even number")
    else:
        print (i,"is a odd number ")



n=str(input("enter a string  = "))
vowel="aeiou"
count=0
cons=0
for i in n:
    if i in vowel:
        count=count+1
        print(i)
    else:
        cons=cons+1
print("total number of vowel in this string is =",count)
print("total number of cons in this string is ",cons)

n=int(input("enter a number"))
for i in range(1, n+1):
    if (i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0):
        print(i)

    

#fibonnacci number 

n=int(input("enter a number "))

a=0
b=1
for i in range(n):
    print(a,end=" ")
    temp=a
    a=b
    b=temp+a


n=int(input("enter  a number = "))

for i in range(1,n+1):
    print("@"*i)


n=int(input ("enter the number of rows = "))


for i in range(1,n+1):
    space=n-i
    star=2*i-1
    print(" "*space+"*"*star)
#for i in range(n-1,0,-1):
    #space=n-1
    #star=2*i-1
    #print(" "*space+"*"*star)
for i in range(n-1, 0, -1):
    space = n - i
    star = 2*i - 1
    print(" " * space + "*" * star)


#reverse number print korte use kora hoy onk ta c++ ar moto start,end ,step (increment or decrement value korte use kora hoy)

#n=int(input("enter a number = "))
##for i in range(n,0,-1):
    #print(i)

    


n=int(input("enter a number = "))


for i in range (1,n+1):
    space=n-i
    print(" " * space,end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()



n=int(input("enter  a number = "))


for i in range (1,n+1):
    print("*"*i)

for i in range(n-1,0,-1):
    print("*"*i)
    



n=int(input("enter  A  number = "))


for i in range(1,n+1):
    
  for j in range(i+1):
    
    if j%2==0:
      print("*"*j)
    else:
      print(j)

      


for i in range(1,12):
    if i==11:
       break
    print("5*",i,"=",5*i)



def calculateAvg(a,b):
    a=a+b 
    print("the sum  of two number is = ",a) 

a=int(input("enter a number = "))
b=int(input("enter a number = "))

calculateAvg(a,b)



def maximum(a,b,c):

    if a>b and a>c:
        print("maximum number is ", a)
    elif b>a and b>c :
        print("maximum number is b ",b)
    else :
        print("maxium number is ",c)

def sumOf(n):
    sum=0
    for i in range(n):
        sum=sum+i

    print(sum)
#variable length arguments 

def avg(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("average is :",sum/len(numbers))

#keyword length arguments 

def average(a=6,b=2):
    print("the average is ",(a+b)/2)



n1=int(input("enter first  number =  "))
n2=int(input("enter 2nd   number =  "))
n3=int(input("enter 3rd  number =  "))

maximum(n1,n2,n3)
sumOf(n1)
avg(n1)
average()


n=["arman","shaowaon","mango"]
for i in n:#aibhabe shudu list print korte pare number ar khetre range()use korte hobe 
    print (i)
n=5

for i in range(1,n+1):
    print(i)

    """

#if a number is a prime or not prime 

def prime(n):
 if n>1:
    for i in range(2,n):
        if n%i==0:
            print("not prime number ")
            break
    else :
            print("prime number ")
 else:
    print("not prime number")


n=int(input("enter a number "))

prime(n)
