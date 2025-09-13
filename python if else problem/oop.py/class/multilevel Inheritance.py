class animal:
    def __init__ (self,name,speci):
        self.name=name
        self.speci=speci

    def showdetails(self):
        print(f"name : {self.name}\nSpeciecs is : {self.speci}")

class dog(animal):
    def __init__ (self,name,breed):
     animal. __init__ (self,name,speci="dog")
     self.breed=breed
     def showdetails(self):
        animal.showdetails(self)
     print(f"breed is : {self.breed}")

class golden(dog):
  def __init__ (self,name,colour):
    dog. __init__ (self,name,breed="golden")

    self.colour=colour

  def showdetails(self):
     print(f"colour : {self.colour}")

o=golden("tommy","black")
o.showdetails()



     

        
              