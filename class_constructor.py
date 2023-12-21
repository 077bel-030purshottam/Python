class DemoClass:
    a=10
    def __init__(self):
        print("hi bro how are u ")
    def ShowValue(self):
        print(self.a)
        self.c=self.a*self.a
        print(self.c)
    def print_value(self):
        print("learn python fast ")

    def pass_argument(self,a,b):
        print(a+b)

obj=DemoClass()
obj.ShowValue()
obj.print_value()
obj.pass_argument(10,60)















