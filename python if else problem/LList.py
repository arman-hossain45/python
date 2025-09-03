# # # #list are mutable 

# # # s1=[34,56,"arman",True] #here t is must capital alphabet
# # # # print(s1[0])
# # # # print(s1)

# # # # print(s1[-2])


# # # # if 89 in s1 :
# # # #     print("yes")
# # # # else :
# # # #     print("no")

# # # marks=[3,4,5,"arman","eleveen","f1"]
# # # print(marks)
# # # print(marks[:])
# # # print(marks[1:])

# # # print (marks[1:-1])
# # # print(marks[0:3:])

# # #list comprehension
# # # lst=[i for i in range (4)]
# # # print(lst)

# # lst2=[i*i for i in range(10)if i%2==0]
# # print(lst2)

# names=["milo","sarah","arman","meem","alex","h"]
# names_with=[item for item in names if len(item)<2]
# print(names_with) 

#list method in python 

#lst=[1,2,3,4,5,6,6,7,8,99,10]

# print(lst)
# lst.append(7)
# print(lst)
# lst.sort()
# print(lst)
# lst.sort(reverse=True)
# print(lst)
# lst.index(1)# here rise a value error in this step because 100 is not on this list 
# print(lst)

ar=[12,45,78,45,20]


print(ar.insert(1,1))
# we can do slicing as useally use 
