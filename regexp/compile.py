import re
p = re.compile('...')
m = p.match('string goes here')
if m:
    print ('match found: ', m.group())
else:
    print ('no match')


q = re.compile(r'\d+')
r = q.findall('12 fjgfjdkhgklf gfdg, 11 hjfkhdgkj')
#print(r.group())
if r:
    print(r)