
# difference betwen list and tuple
alist = [30,40,45]
alist[0] = 300
print(alist)

# tuple
atup = (34,34,43)
#atup[0] = 340
print(atup)
alist = list(atup)  # converting to list
alist[0] = 340      # making changes
atup = tuple(alist) # reconverting back to tuple
print(atup)