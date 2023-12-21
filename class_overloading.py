"""function overloading means function  name is same 
 but different parameters is passed """


class student:
    def display(self, name=""):
        print("welcom to python class " + name)


class teacher(student):
    def display(self, name=""):
        super().display()
        print("welocime to the programming class " + name)


obj = teacher()
# obj.display()
obj.display("purshottam")
