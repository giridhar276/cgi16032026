# for loop
# range(start,stop,step)
for i in range(1,11):
    print(i)
print("***************************")
# range(start,stop,incremental)
for i in range(1,11,2):
    print(i)
print("***************************")
for i in range(2,11,2):
    print(i)
print("***************************")
name = "python"
for char in name:
    print(char)
print("***************************")
alist = [10,20,30]
for val in alist:
    print(val)
print("***************************")
atup = (10,20,30)
for val in atup:
    print(val)
print("***************************")
book = {"chap1":10 ,"chap2":20}
# display keys
for k in book.keys():
    print(k)
print("***************************")
# display values
for v in book.values():
    print(v)
print("***************************")
# dipslay k,v at a time
for k,v in book.items():
    print(k,v)