# 异常:BUG
import os
"""

"""

os.chdir("测试")
"""
语法:
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
"""
try:
    """可能会出现错误的代码"""
    f = open('text.txt', "r")
except:
    f = open('text.txt', "w")
# 捕获异常:如果尝试捕获异常类型和异常类型不一致，就无法捕获
try:
    print(num)
except NameError:
    print('有错误')
# 允许捕获多个指定异常, 通过as 变量 获取描述信息
try:
    print(1/0)
except (NameError, ZeroDivisionError) as result:
    print(result)
# 捕获所有异常 Exception是所有程序异常类的父类
try:
    # print(1/0)
    print(num)
except Exception as result:
    print(result)
# 异常中的else
try:
    print(1)
    #会打印1
except Exception as result:
    print(result)
else:
    print("没有异常")
    #没有异常也会打印1
finally:
    """无论是否异常都要执行的代码，用于关闭文件"""
    f.close()
