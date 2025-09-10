#update age by getter setter method 

class person:
    def __init__ (self,name,age):
        self.__name=name#private variaable
        self.__age=age#private variable

    @property#getter method to read data
    def age(self):
        return self.__age
    @age.setter
    def age(self,newAge):
        if newAge>=0:
            self.__age=newAge
        else:
            print("age does not negative ")

#create an obj of this code\

p=person("arman",200)

print("current age :",p.age)

#settwr method to change data
p.age=25
print("update  age is :",p.age)