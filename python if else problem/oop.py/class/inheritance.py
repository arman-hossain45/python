#inheritance 

class parent:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showdetails(self):
        print(f"the name of the student is {self.name}\nID of the student is {self.id}")


class child(parent):
    def section(self,sec):
        self.sec=sec
        print(f"the section is {self.sec}")


a=child("arman",56)

a.showdetails()#we call parent class method by child class in this child class object 
a.section("csit")