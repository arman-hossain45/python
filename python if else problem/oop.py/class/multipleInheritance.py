class employee:
    def __init__ (self,name):
        self.name=name
    def show(self):
        print(f"The name is {self.name}")

class dancer:
    def __init__ (self,dance):
        self.dance=dance
    def show(self):
        print(f"The dancer is {self.dance}")

class dancerEmployee(dancer,employee):  #in multiple inheritance whose class is first inherit this method is first call 
    #dancer first inherit so dancer first call here dancer show mwthod then another 
    def __init__ (self,dance,name):
        self.dance=dance
        self.name=name

o=dancerEmployee("rapper","kollani")

o.show()

