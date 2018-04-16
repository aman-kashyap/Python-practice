while True:
    try:
        fp=open("example.txt")

        x= int(input("Please enter a number: "))
        b=0
        if b==0:
            raise ValueError("This is my message")
        y=4/b
        if (x>20) :
            break
    except ValueError as e:
        print("please enter integer number ",e)
        x= int(input("please enter a number :"))
        if (x>20):
            break
    except (ZeroDivisionError,TypeError):
        print("cannot divide by zero")

        print(x/5)
        break
    
    except:
        print("generalised Exception")
     
    finally:
        print ("in finally block")
        fp.close()

print(x)
