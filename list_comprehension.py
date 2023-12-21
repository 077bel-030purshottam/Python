
# ways of creating list in python 
l = []
for a in range(1, 101):
    # print(a)
    l.append(a)


print(l)
# **************************************************

# another ways to create list in python using python comprehension 

n=[m for m in range (1,101) if  m %2==0]
print("\n",n)
st1="purshottam"

list100=[l  for l in st1]
print(list100)
print(type(list100))


















