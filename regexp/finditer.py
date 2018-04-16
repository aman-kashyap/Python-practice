import re 

p=re.compile(r'\d+')
m = p.finditer('12 bjdgfjshj jehfkjrhf ,11 ... 10 ...')

#print (iterator.())
#print (iterator.group())
for min in m :
    print ('match found: ', min.group())
    print(min.span())
    #print ('no match')