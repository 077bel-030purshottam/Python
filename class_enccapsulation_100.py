class student:
    __name = "purshottam"

    def __init__(self):
        print(self.__name)
        self.__display()

    def __display(self): # private methoda can not be used with the help of the object  it must be called in constructor
        print("hello bro how are u ")


obj = student()
# print(obj.__name) this is not allowed in the case of the private variable


