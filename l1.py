age=int(input("enter age"))
if age<5:
    print("you are in kindergarden")
elif age<10:
    print("you are in primary")
else:
    print("u are in highschool")

x=int(input("enter a number x :"))
y=int(input("enter a number y :"))
z=int(input("enter a number z :"))

if x>y and x>z:
    print("x is maximum ")
elif y>x and y>z:
    print("y is max")
else:
    print("z is max")


#i==x if x>y and x>z elif i==y if y>x and y>z else z
 #   print i