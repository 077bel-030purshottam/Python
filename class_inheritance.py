class A:
    def dispaly(self):
        print("class A ")


class B(A):
    def displayB(self):
        print("class B")

class C(B):
    def displayC(self):
        print("class C")


obj=C()
obj.dispaly()
obj.displayB()
obj.displayC()


