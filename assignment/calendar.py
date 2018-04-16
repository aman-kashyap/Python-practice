# Write a program that asks the user how many days are in a particular month, and what day of the week 
# the month begins on (0 for Monday, 1 for Tuesday, etc), and then prints a calendar for that month.
# For example, here is the output for a 30-day month that begins on day 4 (Thursday):
# S M T W T F S
#         1 2 3
# 4 5 6 7 8 9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30

month=["january","february","march","april","may","june","july","august","september","october","november","december"]
days=[31,28,31,30,31,30,31,31,30,31,30,31]
week=['mo','tu','we','th','fr','sa','su']

i=1
j=1

if 0<i<=12:
    i=int(input("Enter which month you want to print: "))
    print("you chose :",month[i-1],"and number of days are :",days[i-1])
if 0<j<=7:
        j=int(input ("which day the month begins :"))
        print("you chose : ",week[j-1])

a=(days[i-1]/7)+1
b=7
c=[0]*a

for x in range(0,days[i-1]):
    c[x]= [0]*b
    print(c)
    #print (x+1,end=" ")
    






