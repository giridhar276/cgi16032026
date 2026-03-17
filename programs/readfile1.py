
# method1
fobj = open("languages.csv","r")
for line in fobj:
    print(line.strip())
fobj.close()


# method2
# fobj.readlines() -----> list
fobj = open("languages.csv","r")
print(fobj.readlines())
fobj.close()


# method3
# fobj.read() ----> string
fobj = open("languages.csv","r")
print(fobj.read())
fobj.close()

# method4
import csv  # builtin library
fobj = open("languages.csv","r")
reader = csv.reader(fobj)
for line in reader:
    print(line)

# method5
# in terminal :   pip install pandas
import pandas  as pd   # third party library 
df = pd.read_csv("languages.csv")
print(df)