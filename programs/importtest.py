
# method1:  all the methods are imported to your programspace
import math 
print(math.log(1))
print(math.tan(1))


# method2: importing with alias name
import math as m 
print(m.sin(1))
print(m.factorial(4))

# method3: iporting required methods only 
from math import log,tan
print(log(1))
print(tan(2))