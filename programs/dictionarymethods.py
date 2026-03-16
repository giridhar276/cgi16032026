# dictionary  # key-value pairs
book = {"chap1":10 ,"chap2":20,"chap3":30}
# display individuval value
print(book["chap1"]) # 10
print(book["chap2"]) # 20
# crate new key-value pairs
book["chap4"] = 40
book["chap5"] = 50
book["chap6"] = 60
print(book)

# display ONLY Keys
print(book.keys())

# dipslay values
print(book.values())

# display items
print(book.items()) # key and value makes an item

# remove key-value from dictionary
book.pop("chap1") # chap1-10 wil be removed from dictionary
print(book)

book.popitem()    # will remove last key-value pair
print(book)

################## joining dictionaries

book = {"chap1":10 ,"chap2":20,"chap3":30}
newbook = {"chap4":40 ,"chap5":50}
finalbook = {**book,**newbook}    
print("final dictionary :", finalbook)

# existing book is getting updated
book.update(finalbook)

# if key is not found.. will throw error
#print(book["chap9"])
print(book.get("chap9"))  # if key is not found.. it returns None
# converting list to dictionary
data = ["name","Age","city"]
mydict = dict.fromkeys(data) # { "name":None, "Age": None,"city": None}
print(mydict)
mydict = dict.fromkeys(data,0)
print(mydict)