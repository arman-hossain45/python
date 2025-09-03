d={"arman":"human being","age":25}
print(d)
print(d["arman"])
print(d["age"])
d["age"]=26
print(d["age"])#udate age 
dictionary={34:"arman",
            35:"hossain",
            36:"meherun nesa meem",
            37:"yeanty"}
print(dictionary)
print(dictionary[34])
print(dictionary[35])
print(dictionary[36])
print(dictionary[37])#we can call by there id to a specific member in a dictionary

#another way toprint a dictionanary
print(dictionary.keys())#it will print all the keys of the dictionary which is 34,35,36
print(dictionary.values())#it will print all the values of the dictionary which is arman,hossain,meem,yeanty
print(dictionary.items())#it will print all the items of the dictionary in a tuple form
dictionary[38]="sajib"#it will add a new member in the dictionary
print(dictionary)
print(len(dictionary))#it will print the length of the dictionary
dictionary.pop(38)#it will remove the member of the dictionary by there key value
print(dictionary)
print(dictionary.get(34))#it will print the value of the key 34
print(dictionary.get(39))#here there is no key 39, so when we run a code it doest not show any error it show only none 
print(f"the value corresponding to the key  is {dictionary.get(34)}")#it will print the value of the key 34

for i in dictionary:
    print(f"the value corresponding to the key {i} is {dictionary[i]}")#it will print all the key and value of the dictionary

# method in dictionary

a={122:45,34:78,89:90,67:56}
b={1:2,3:4,5:6}
a.update(b)#it will update the value of a with b
print(a)#show the hole dict a+b
#a.clear()#it will clear the whole dictionary aq
#print(a)#{}show only this empty

a.pop(122)
print(a)#it will remove the key 122 and its value from the dictionary a
a.popitem()#it will remove the last item of the dictionary
print(a)
#del in this method it delete the hole dictionary smoothly 
