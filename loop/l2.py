num =int(input("enter a number :"))
#num=5
i=2

while i < num:
    if num %i ==0:
        print("not prime")
        break
    i=i+1
else:
        print("prime")


for i in range (10,41,10):
    print (i)
