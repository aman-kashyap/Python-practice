a=12
b=a
a=15
print(a,b)

x=['a','b','c']

y=x
x.append('d')
print(x)
print(y)


z=x.copy()
z.append('E')
x.append('p')
print(x)
print(y)
print(z)
