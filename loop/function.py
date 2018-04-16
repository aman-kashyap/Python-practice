def myfunction(a=12,b=13):
    print(a,b)
    return a+b

x=myfunction()
print(x)
x=myfunction(23)
print(x)
x=myfunction(23,10)
print(x)
