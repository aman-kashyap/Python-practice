l1=['a','b','c']
l2=[10,20,30]
#l3=['@','#']
for i,j in zip(l1,l2):
    print(i,j)


for i,j in enumerate(l1,start=10):
    print(i,j)

for i in reversed(l1):
    print(i)

for i in sorted (l1):
    print(i)

for i,j in zip(enumerate(l1,start=10),l2):
    print(i,j)