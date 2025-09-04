# x = 5
# print(x)

# def myfunc():
#     x = 10
#     print(f"the local x is {x}")
#     print("hellow world")

# print(f"the global x is {x}")
# myfunc()
# print(f"the global x is still {x}")

x=10
def myfunc():
    y=5
    print(y)
    global x#we change the value of global variable x inside the function
    x=15#it will change the value of global variable x
myfunc()
print(x)
#print(y)# print(x)
# print(y) #it will give error because y is local variable and we are trying to access it outside the function