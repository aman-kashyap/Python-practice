global_var="This is global variable"

def myfunction():
    global global_var
    var_outside= 'outervar'
    global_var="zzzz"
    def inside():
        nonlocal var_outside
        var_inside ='inside'
        var_outside="In inside function"
        print(var_outside)
        print(global_var)
    inside()
    print (var_outside)
    print("inside function variable", var_inside)


myfunction()
print(global_var)