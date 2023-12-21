class area:
     def find_area(self,a=None,b=None):
          if(a!=None and b!=None):
               print("the area is ", a*b)
          elif (a!=None):
               print("the area is ",a*a)

          else:
               print("the area is zero ")


obj=area()
obj.find_area()
obj.find_area(10)
obj.find_area(10,20)


























