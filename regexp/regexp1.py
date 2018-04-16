# regx to find line where 3rd character is c and 5th is p and ends with xyz
# ^{2}c{1}p.*{xyz}\$
# regx to find all lines which contains 1st 3 as aplpha, 5 digit some where and ends with p
# ^[A-Za-z]{3}.*\d{5}.*p$

import re

if re.match('abc', 'abc xyz pqr', (re.I | re.M)):
    print ("match found")
else :
    print ("match not found")
if re.search('abc', 'abc xyz pqr', (re.I | re.M)):
        print ("match found")
else :
    print ("match not found")
if re.match('abc', 'xyz abc pqr'):
        print ("match found")
else :
    print ("match not found")

if re.search('abc', 'xyz abc pqr'):
    print ("match found")
else :
    print ("match not found")

