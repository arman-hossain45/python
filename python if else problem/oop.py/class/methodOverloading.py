class area:
   

    def areafind(self,a=None,b=None):
     if a!=None and b!=None:
      print(a*b)

     elif a!=None:
        print(a*a)

     else:
        print("nothing")

obj=area()
obj.areafind()
obj.areafind(10)
obj.areafind(10,20)

