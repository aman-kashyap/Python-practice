str12 ="This is my string, to replace my string"
str1=str12.replace("my","our",1)
print(str1)
print(str12)
print("Position",str12.find("my",9))
print("Position",str12.find("aaaaa"))

find= str12.find("is")
print("search from 0",find)
find= str12.find("is",4)
print("search from 4",find)
find= str12.find("is",7)
print("search from 7",find)

print (str12[0:7:2])
print (str12[0:7])
print (str12[:3])
print (str12[2:])
print (str12[::-1])
print ("length :", len(str12))

print(str12.split("s"))

print('x' not in 'apple')
print('i' in 'apple')
print('p' in 'apple')

#mystring=' bbabacabc test string abcabcbbbb '
#print(" strip white space")

mystring1 =' anagha goes to school wiht raman'
print ("strip an", mystring1.strip('an'))

p=10
x="abc"
y="pqr"
z="xyz"
print ("this is number " + str(p))
print (x,y,z)
print(x,y,z, sep=":")
print(x,y,z, sep=":",end="")
print("hello")
print("hello next")

print("--".join(["aaa","bbb","ccc"]))


gender = input("enter son or daughter")
maths =input("enter maths marks")
java = input("enter java marks")

print("your {1} scored {0} marks in maths test and {2} in java test " . format(maths,gender,java))

print("%s %s %s %7.2f %5d" %("kishori", "Deepali", "Ashwini", 1/3, 30))


