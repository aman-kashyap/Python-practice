#set 

x={"a","b","c","d","e",'f','g'}
y={"b","c"}
z={"c","d"}

print(x.difference(y))
print(x-y)
print(x.difference(y).difference(z))


x.discard("a")
print(x)
#x.remove("a")


print("union",x.union(y))

print("x|y same as x.union(y)",x|y)

print(x.intersection(y))
print(x&y)

print(x.isdisjoint(y))

print(x.issubset(y))
print(y<x)

print(x.issuperset(y))
print(x>y)

print(x.pop())



