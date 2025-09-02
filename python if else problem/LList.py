# # #list are mutable 

# # s1=[34,56,"arman",True] #here t is must capital alphabet
# # # print(s1[0])
# # # print(s1)

# # # print(s1[-2])


# # # if 89 in s1 :
# # #     print("yes")
# # # else :
# # #     print("no")

# # marks=[3,4,5,"arman","eleveen","f1"]
# # print(marks)
# # print(marks[:])
# # print(marks[1:])

# # print (marks[1:-1])
# # print(marks[0:3:])

# #list comprehension
# # lst=[i for i in range (4)]
# # print(lst)

# lst2=[i*i for i in range(10)if i%2==0]
# print(lst2)

names=["milo","sarah","arman","meem","alex","h"]
names_with=[item for item in names if len(item)<2]
print(names_with)