l = []
while True:
    c = int(
        input(
            """

      1 push element
      2 pop first  element
      3 front element
      4 last element
      5 display element
      6 exit                            


"""
        )
    )
    if c == 1:
        n = int(input("enter the value "))
        l.append(n)
        print(l)
    elif c == 2:
        if len(l) == 0:
            print("empty queue ")
        else:
            del l[0]
            print(l)

    elif c == 3:
        if len(l) == 0:
            print("empty queue")

        else:
            print("first  element is ", l[0])

    elif c == 4:
        if len(l) == 0:
            print("empty queue")

        else:
            print("last  element is ", l[-1])

    elif c == 5:
        print("display queue ", l)

    elif c == 6:
        print("out of the loop ")
        break

    else:
        print(
            """invalid choice 
              plz enter valid choice """
        )
