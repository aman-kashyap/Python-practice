import re

p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
None
print(p.search ('one subclass is'))
None