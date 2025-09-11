class porter:
    company="apple"

    def show(self,name):
        self.name=name
        print(F"The employee  name is : {self.name}\nCompany name is {self.company}")
    @classmethod
    def changeCompany(cls,newcompany):
        cls.company=newcompany

a=porter()
a.show("arman")
a.changeCompany("tesla")
a.show("arman")
b=porter()
b.show("shawon")
