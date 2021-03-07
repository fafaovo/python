# 模块和包
# 方法1:import 模块名
# import math
# print(math.sqrt(9))

# 方法2:from 模块名 import 功能1，功能2[此处如果使用*则代表全部]
# 这里可以省去调用模块名
# from math import sqrt
# from math import *
# print(sqrt(9))

# 模块定义别名 import 模块名 as 别名[将来只能使用这个别名，不能使用原本的名字]
# import math as shuxue
# print(shuxue.sqrt(9))

# 功能定义别名 from 模块名 import 功能 as 别名
from time import sleep as sp
print("hello")
sp(2)
print("world")



