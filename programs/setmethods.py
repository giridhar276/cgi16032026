
aset = {10,10,10,20,20,20,30}
bset = {30,30,30,40,40,40,50}

print(aset)
print(bset)

aset.add(30)
print(aset) # no difference
aset.add(40)
print(aset)

print(aset.union(bset))
print(aset.intersection(bset))
print(aset.difference(bset))

print(aset.difference_update(bset))