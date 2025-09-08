#in c or c++ if we want to see index we use a temporay variable which is declared as 0 
#and we increase the value one by one 

marks=[45,67,89,90,23]
index=0
for mark in marks:
    print(mark)
    
    if index==2:#when index is 2 then print arman nice 
        print("arman nice")
    index+=1# increase the temporay variable




#but i py we dont declair index =0 

for index,mark in enumerate(marks):#here we use enumerate function
    print(mark)
    if index==2:#when index is 2 then print arman nice
        print("arman nice")


fruits=["apple","banana","mango","grapes"]
for index,fruit in enumerate(fruits):
    print(index,fruit)# we want to see index with fruits 
    