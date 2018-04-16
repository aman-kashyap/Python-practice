def method11(x):
    print (x)
    print ("In method 11")

def method22( x=45, y= "aaa"):
    print (x,y)
    print ("In method 22: ")
    print (__package__)

def __mymethod1__(c):
    print (c)
    print ("In __mymethod 2")

if __name__ == "__main__":
    print("This is main module")
    print("will get executed only if run as script")
    method22()
