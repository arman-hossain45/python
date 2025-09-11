#static method in python 

class math:
    def __init__(self,num):
        self.num=num

    def addToNum(self,n):
        self.num=self.num+n

    @staticmethod
    def add(a,b):
        return a+b
# in normal class that operation we do normally  
a=math(5)
print(a.num)
a.addToNum(6)
print(a.num)

# for static method we can do like this 

print(math.add(1,2))# we can access this method without create class object  direct access this method 