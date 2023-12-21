x = "purshottam "  # global variable


def myname():
    print(" my name is " + x)
    global y
    y="my home is at haripur "


myname()
print(y)
