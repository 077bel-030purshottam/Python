"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneTypeA

"""
name = " my name  is purshottam "
s = 10
f = 50.12
com = 1 + 2j
print(name, s, f, com)

l2 = ["mango", "banana", "apple"]
t1 = ("hell", "my name is ", "purshottam ")
ran = 10
print(l2, t1, ran)

d1 = {"name": "purshottam ", "age": "10"}
s1 = {"my name is ", "purshottam "}
print(d1, s1)
m = frozenset(("hello", "how are u "))
print(m)
g = bool(10)
print(g)
h = bytes(2)
print(h)
i = bytearray(5)
print(i)
j = memoryview(bytes(120))
print(j)


