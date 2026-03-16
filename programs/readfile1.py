
# method1
fobj = open("languages.csv","r")
for line in fobj:
    print(line.strip())
fobj.close()


# method2
fobj = open("languages.csv","r")
print(fobj.readlines())
fobj.close()


# method3
fobj = open("languages.csv","r")
print(fobj.read())
fobj.close()

# method4
import csv 
fobj = open("languages.csv","r")
reader = csv.reader(fobj)
for line in reader:
    print(line)

# method5
import pandas  as pd
df = pd.read_csv("languages.csv")
print(df)