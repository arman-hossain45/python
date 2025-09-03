tup=(1,2,3,4)#tuple are unchangable when we cerate a tuple it cannot be change 
print(type(tup),tup)
#when we give this type of cammand it show error

#tup[0]=90
#print(tup)#show error this modification


#print(tup[-1])

if 342 in tup:
    print("yes 342 is in the tuple")
else :
    print("not in this tuple list")

#slicing of a tuple 
tup2=tup[1:4]
print(tup2)
#tuple are same as usall list but in list we can change the size and 
#value also but in tuple we cant change it 

#opearation in tuple we convert tuple into list for add and pop element in this list 
countries=("spain","canada","italy","usa","uk","belgium")

temp=list(countries)
print(temp)
temp.append("london")#here add london in the list 
print(temp)
temp.pop(3)
print(temp)#here pop element in the list 

temp[2]="finland"
countries=tuple(temp)
print(countries)# 2 no index we input a country name is finland

#marge tuple 
t1=(1,22,3,345,67)
t2=(12,34,56,78,89)
t3=t1+t2
print(t3)

tup=(0,1,2,3,3,3,6,7,8,9,10)
res=tup.count(3)
print("count is 3 in tuple is",res)

print(tup.index(3,4,8))#(element,start,end)(3 element,start index 4,end index is 8)



