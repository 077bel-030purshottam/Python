class A:
    def dispalyA(self):
        print("class A ")


class B():
    def displayB(self):
        print("class B")

class C(A,B): # inheriting class A and B in one class

    def displayC(self):
        print("class C")


obj=C()
obj.dispalyA()
obj.displayB()
obj.displayC()


