a=[1,2,3,4,5,6]

print(dir(a))

print(a.__add__)

#which method work all show in this library



# ['__add__', '__class__', '__class_getitem__', '__contains__',
#   '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
#     '__format__', '__ge__', '__getattribute__', '__getitem__', ''
#     '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', 
#     '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', 
#     '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
#     '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', 
#     '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 
#     'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
  


  #downder method in pytho it work like this 
a = [1, 2, 3, 4]
print(len(a))         # 4
print(a.__len__())    # 4  → `len(a)` 


a = [10, 20, 30]
print(a[1])           # 20
print(a.__getitem__(1))  # 20  → `a[1]`


a = [1, 2, 3]
a[0] = 100
print(a)              # [100, 2, 3]

# Equivalent using dunder method
a.__setitem__(1, 200)
print(a)              # [100, 200, 3]


