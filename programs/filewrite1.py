
# if the file is not existing .. file gets created
# if the file is already existing.. it overwrites

# regular way # traditional way
fobj = open("customers.txt","w")
fobj.write("this is first line\n")
fobj.write("this is second line\n")
fobj.writelines(["unix","java","C","oracle\n"])

for val in range(1,10):
    fobj.write( str(val)  + "\n")
fobj.close()

# pythonic way   # modern way
# context manager
# if any line begins using with keyword .. it is called as context manager
# Advantage: file gets closed automatically
with open("customers.txt","w") as fobj:
    fobj.write("this is first line\n")
    fobj.write("this is second line\n")
