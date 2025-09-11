# class A:
#     companyname="apple"#class variable 

#     def __init__(self,name):
#       self.name=name
#       self.raise_amount=200

#     def showdetails(self):
#        print(f"the name of the employee is {self.name}\nRaise amount in {self.companyname} is {self.raise_amount}")
# # we class variable like this in this method wit arguments 

# a=A("arman")
# a.raise_amount=300
# a.companyname="infosis" #we change the company name as a variable name but it dont change another variable name in this 
# #another object we change only this class respectivly but not hole class 

# a.showdetails()
# b=A("karima") 
# b.showdetails()#here it show us the name apple  dont show infosis in this class 


    
class a:
    name="apple"
    def __init__(self,id):
       
        self.id=id

    def show(self):
        print(f"The name of the company is {self.name}\nCompany ID is :{self.id}")


aa=a(23)
aa.show()

bb=a(24)

bb.show()
a.name="google"#change the class variable for every object 
aa.show()#show name is google 
bb.show()#show name is google if we change the name as class respectivly then change the 
#only  object respectivly only not change for every object 

