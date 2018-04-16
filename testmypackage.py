import mypackage.mymodule1
from mypackage import mymodule2
from mypackage.mymodule2 import *
# from mymodule2 import *

mypackage.mymodule1.method1(10)
mypackage.mymodule1.method2()
mypackage.mymodule1.__mymethod__(10)

mymodule2.method11(20)



