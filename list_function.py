l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(l)

# deleting the elements of the list 
del l[0]
print(l)
print(l.pop(3))
print(l)
l.remove(80)
print(l)
l.clear()
print(l)
# ***************************************************

# updating the element of the list 
print("\n updating the valus of the list \n ")
l2=[100,200,300,400,500,600]
print(l2)
l2[0]=1000
print(l2)

# *************************************************
l2.insert(3,12345)
l2.insert(6,12310245)
print(l2)

# ***********************************************
l2.append(369852)
print(l2)
l3=[1,2,3]
l2.append(l3) 
print(l2)

# ************************************************
l2.extend(l3)
print(l2)

# *******************************************************



