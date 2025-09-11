class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, st):
        parts = st.split("-")          
        return cls(parts[0], parts[1]) 

st = "john-10000"
a = Employee.fromStr(st)   
print(a.name)    
print(a.salary)  
