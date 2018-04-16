import re

multilinestring="""something somewhere someotherthing"""
if(re.match("some",multilinestring)):
    print("found some")
else:
    print("not found some")
print (re.match('someother',multilinestring))

print (re.match("^someother",multilinestring,re.M))
print (re.search("someother",multilinestring,re.M))

print (re.match("^somew",multilinestring,re.M))

print (re.search("^somew",multilinestring,re.M))

print (re.search("^someother",multilinestring,re.M))



m= re.compile('things$',re.M)

print ("no match ", m.match(multilinestring))
print ("match found ", m.match(multilinestring, pos=4))

text="How are u ? use sub u"
print (text)
print(re.sub(r'\b[uU]\b','you',text,count=0))
print(m.search(multilinestring,re.M))