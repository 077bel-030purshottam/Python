l = []
while True:
    c = int(
        input(
            """
      1 push element
      2 pop element
      3 peek element
      4 display element
      5 exit                            

"""
        )
    )
    if c == 1:
        n = int(input("enter the value "))
        l.append(n)
        print(l)
    elif c == 2:
        if len(l) == 0:
            print("empty list")
        else:
            n = l.pop()
            print(l)

    elif c == 3:
        if len(l) == 0:
            print("empty list")

        else:
            print("last element is ", l[-1])

    elif c == 4:
        print("dispaly stack ", l)

    elif c == 5:
        exit()
    else:
        print(
            """invalid choice 
              plz enter valid choice """
        )
