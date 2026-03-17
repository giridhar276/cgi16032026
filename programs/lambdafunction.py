# regular way
# every process contains system calls
def display(a,b):
    c  = a +b
    return c
output = display(10,20)
print(output)


# pythonic way
# lambda function : lambda is the replacement of single liner function
# syntax:
# functioname = lambda variables : expression

display = lambda a, b: a + b
output = display(10,20)
print(output)


display = lambda *args: sum(args)
output = display(10,20,30,40,50,60,70,80,90,100)
print(output)



# 1. Max of two numbers
maximum = lambda a, b: a if a > b else b
print(maximum(10, 20))  # 20

# 2. Pass or Fail
result = lambda marks: "Pass" if marks >= 35 else "Fail"
print(result(30))  # Fail



# 4. Positive, Negative or Zero
sign = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(sign(-5))  # Negative




alist =  ["python","unix","C","java"]  
# [6,4,1,4]
# map(function,iterable)
print(list(map(lambda x: len(x),alist))) #[6,4,1,4]

alist = [1,2,3,4]
print(list(map(lambda x: str(x),alist)))