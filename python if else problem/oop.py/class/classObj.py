# # class person:
# #     name="armna"#class variable 
# #     occ="ml"
# #     networth="100"

# #     def display(self):#class method
# #          print(f"my name is {self.name}, and my occ is {self.occ}, my net worth is {self.networth}")

# a=person()#class object
#  a.display() #call class method in this function call 

# class person:
#     def __init__ (self):
#         print("hey my name is Arman")


# a=person()

# class f1:
#     def __init__ (self,name,occ):
#         self.name=name#set value by constractor 
#         self.occ=occ
#     def info(self):
#         print(f"hey my name is {self.name}, and my occupation is {self.occ}")

# a=f1("arman","ml engineer")
# a.info()
# b=f1("karina","data analysist")
# b.info()
# for i in range(4):
#     b.info()

#return fuc to another function 

# def test(num):

#     if num==0:
#         return print
#     else:
#         return sum

# #ret=test(1)
# print(test(1))

#one fun to another func as aargument 

# def test(fun):
#     fun("in the function")


# test(print)

#topic decorator

# def test(fun):
#     def test2():
#         print("first line of test2")
#         fun()
#         print("2nd line of test2")

#     return test2 
    
    
# যদি return test2 না লিখতে, তাহলে test() কোনো ফাংশন রিটার্ন করতো না (মানে None রিটার্ন করতো)।

# ফলে hello = test(hello) করার পর hello এর ভ্যালু হয়ে যেতো None, আর তুমি hello() কল করলে এরর পেতে।

# তাই return test2 দরকার, যাতে পুরানো ফাংশনকে নতুনভাবে মোড়ানো যায়।
#here we can also write like that 


# @test
# def hello():
#     print("hello world")

#hello=test(hello)
# hello()


#Create a class Car with attributes like brand, model, and year. Write a method to display the car’s details.

# class car:
#     def __init__ (self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year

#     def info(self):
#         print(f"car detais is {self.brand},brand model is {self.model}, and year is {self.year}")

# value=car("x_corolla","fb23","2014")
# value.info()


#Define a class Student with attributes name, roll, and marks. Write a method to check if the student has passed (marks ≥ 40)
# class student:
#     def __init__ (self,name,roll,marks):
#         self.name=name
#         self.roll=roll
#         self.marks=marks

#     def info(self):
#         if self.marks>40:
#             print(f"The name of the student {self.name}\n Roll is {self.roll}\n PASS")

#         else:
#               print(f"The name of the student {self.name}\n Roll is {self.roll}\n FAIL")


# value=student("Arman",231061008,90)
# value.info()

#Create a class Book that stores title, author, and price. Add a method to apply a discount.

# class book:
#     def __init__ (self,title,author,price):
#         self.title=title
#         self.author=author
#         self.price=price
 
#     def discount(self,discount):
        
#         discount=self.price*(discount/100)
#         self.disprice=self.price-discount
#         print (f"Title of the book :{self.title},\nAuthor of the book is {self.author}\nOrginal prize of this book {self.price}\nPrize of the book is after get {discount}taka discount {self.disprice}\n")

# a=book("python","arman",1000)

# a.discount(20)

#Create a class BankAccount with attributes account_number and balance. Implement methods for deposit() and withdraw().


# class BankAccount:
#     def __init__ (self,Ac_no,balance):
#         self.Ac_no=Ac_no
#         self.balance=balance

#     def deposit(self,amount):
#         self.newbalance=self.balance + amount
#         print(f"Account balance is {self.balance}\nDeposit amount is {amount}\nNew amount is {self.newbalance}")

#     def withdraw(self,amount):
#         if self.newbalance>=amount:
#             self.newbalance=self.newbalance-amount
#             print(f"new balance is {self.newbalance}")

#         else:
#             print("Not amount of money so you cant withdraw")

# a=BankAccount(101,2000)

# a.deposit(1000)
# a.withdraw(100)


#Define a class Employee with name, salary, and position. Add a method to give a raise

class employee:
    def __init__ (self,name,salary,position):
        self.name=name
        self.salary=salary
        self.position=position

    def raiseSalary(self,percent):
        self.newsalary=self.salary + self.salary*(percent/100)
        print(f"Employee name is {self.name}\nEmployee salary is {self.salary}\nEmployee position is {self.position}\nEmployee new salary raise {percent}% is {self.newsalary}")

a=employee("Arman",20000,"ML engineer")

a.raiseSalary(20)





