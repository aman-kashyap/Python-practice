# Write another program to read contents from the file
# If designation is
# manager then add bonus=2000 in the salary and display on the screen
# analyst then add bonus=1500 in the salary
# otherwise add bonus=1000 in the salary


f2 = open('empl.dat', 'a' )

#x=""
#for entry in x:
#    x=str(input("Do you want to add more entries (y/n)"))
#    if x=="y":
empno=int(input("Enter the employee no: "))
ename=str(input("Enter the employee name: "))
varsal=int(input("Enter the employee salary : "))
vardesig=str(input("Enter the employee designation: "))

data = ['empno','ename','varsal','vardesig']
f2.write(str(empno) +":"+ ename +":"+ str(varsal) +":"+ vardesig )
#continue

f2.close()

f2 = open('empl.dat', 'r' )

line = f2.readline()

empno, ename, varsal, vardesig = line.split(':')

for  vardesig in data:
    if vardesign=="manager":
        varsal=varsal+2000
        print (data)