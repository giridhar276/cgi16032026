### simple if condition
if 1 < 2 :
    print("condition is true")

### simple if condition
name = "python"
if name.startswith("p"):
    print("its python")
    print("inside")
    print("still inside")
### if-else condition
if name.islower():
    print("string is lower")
else:
    print("string is lower")

##### if-elif-elif-elif-else 
lang = input("Enter any language:")
if lang == "python":
    print("its python")
elif lang == "java":
    print("its java")
elif lang == "oracle":
    print("its oracle")
else:
    print("its someother language")

### check for existence of the item
name = "python programming"
if "program" in name:
    print("its python")

alist = [10,20,30,40]
if 10 in alist:
    print("exists")

book = {"chap1":10 ,"chap2":20}
if "chap1" in book:
    print("key exists")