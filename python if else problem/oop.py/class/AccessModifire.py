# #access modifier  private  accerss modifier 

# class employee:
#     def __init__ (self,):
#         self.__name="arman"


# a=employee()
# print(a.__name)#cannot be accessable

# print(a._employee__name)#acceable through mangling in private data 

# class Employee:
#     def __init__(self):
#         self.__name = "arman"

# a = Employee()
# print(a._Employee__name)  ->arman

#protected

class student:
    def __init__ (self):
        self.name="arman"

    def _fullname(self):
        #protected access modifier 
        return "hello world"

class subject(student):
    pass

obj=student()

obj2=subject()

print(obj._fullname())


print(obj2._fullname())#protected data access by child class 

