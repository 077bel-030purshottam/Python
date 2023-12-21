class A:
    def display(self):
        print("i am in class A")


class B(A):
    def display(self):
        super().display()
        print(" i am in class B ")


obj = B()
obj.display()
