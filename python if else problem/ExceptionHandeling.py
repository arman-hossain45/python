a=int(input("Enter a number: "))
print(f"The number you entered is {a}is")
for i in range(1,11):
    print(f"{a} x {i} = {a*i}")

print("some implementation lines of code")
print("end of thr program ")

#here in this code when we input a string or another digit then it show us a error 
#and another code is not exucute but we want to exucute another code and show us this error message 
#so for this reason we use try and except block

try:
    a=int(input("Enter a number: "))
    print(f"The number you entered is {a}is")
    for i in range(1,11):
        print(f"{a} x {i} = {a*i}")

    
except ValueError:
    print("Invalid input! Please enter a valid number.")
    print("some implementation lines of code")
    print("end of thr program ")

try:
    num=int(input("Enter a number: "))
    a=[5,6]
    print(a[num])
except ValueError:
    print("Invalid input! Please enter a valid number.")
except IndexError:#in this code if iput a range that is not 0,1 then show an error because  here element ar two 
    print("Index out of range! Please enter a valid index.")    
