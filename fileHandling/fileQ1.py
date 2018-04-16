#   Write a program to accept empno,employee name, Salary,Designation
#   empno:empname:salary:designation
#   write the details into a file empdata.dat

f1 = open('empdata.dat', 'w')

empno=int(input("Enter the employee no: "))
empname=str(input("Enter the employee name: "))
salary=int(input("Enter the employee salary : "))
designation=str(input("Enter the employee designation: "))

f1.write(str(empno) +":"+ empname +":"+ str(salary) +":"+ designation )

f1.close()

