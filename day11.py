"""python  Identity Operator

Identity Operators are used to compare the objects,
not if they are equal, but if they are actually the same object,
with the same memory location"""

x = [1, 2, 3]
y = [1, 2, 3]

z = x


print(z is x)
