
#the super keyword in python is used to refer to the parent class .it is specially useful when a class inherits from multiple 
#parent classes and you want to call a method from one of the parent classes 


class parentclass:
    def parentmethod(self):
        print("This is parent method")

class childclass(parentclass):
    def parentmethod(self):
        print("arman")
        super().parentmethod() #personal parentmethod call first
    def childmethod(self):
        print("this is child method")
        super().parentmethod()#orginal parent method call then in this function

cobj=childclass()
cobj.parentmethod()#without super keyword it only  print arman  with super keyword it print arman and this is parentmethod
cobj.childmethod()