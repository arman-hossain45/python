#unordered collection of data item are called set 
s={1,2,3,3,4,55,5,5,6}
print(s)

#set method in python 

#union
s1 = {7, 8,4, 9}
s2 ={1,2,3,3,4}
#print(s1.union(s2))# double value convert in one single value 

#s1.update(s2)
#print(s1)#it will update the value of s1 with s2 which is 1,2,3,4,7,8,9
s3=s1.intersection(s2)
print(s3)# it will print the common value of s1 and s2 empty set there is no value in this terms common 

#symentric difference of a set 
s4=s1.symmetric_difference(s2)
print(s4)# it will print the value which is not common in both set
s5=s1.isdisjoint(s2)
print(s5)# it will print True if there is no common value in both set
s6=s1.issuperset(s2)
print(s6)# it will print True if all item of a particular set are present in the orginal set it return true other 
#wise print false 
s7=s1.issubset(s2)
print(s7)

myset={1,2,3}
myset.add(4)
print(myset) 
myset.update([4,5],{6,7})
print(myset)   
myset.remove(7)
print(myset)
removeitem=myset.pop()
print(removeitem)#randomly delete any item from the set not specific  item 

print(myset)
#myset.clear() print only empty set
#del myset delete the whole set from the code