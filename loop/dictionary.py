super_villains={
    'mogambo':'amrish puri',
    'shan':'k',
    'race':'j',
    'sholay':'A',
    'judva':'S'
}
print(super_villains['mogambo'])

#delete
del super_villains['shan']
print(super_villains)

#update
super_villains['Don']='A'
print(super_villains)

print(len(super_villains))


print(super_villains.get("judva",1))

print("keys are: ",super_villains.keys())

print(super_villains.values())
print(super_villains.items())


print("using items()")

for k,val in super_villains.items():
    print("key:",k," value :", val)

print("using keys()")
for k in super_villains.keys():
    print ("value :", super_villains[k])
    