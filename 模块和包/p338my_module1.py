# import my_module1 as mm
# print(mm.add(12, 13))
"""
当导入一个模块时，python搜索顺序
1.当前目录
2.不在当前目录，则搜索shell变量PYTHONPATH的目录
3.如果都找不到，python会查看默认路径，UNIX默认路径为/usr/local/lib/python/

自己的文件名不要和已有模块名重复,否则导致模块功能无法使用
使用from模块名import功能的时候，如果名字重复，调用的是最后定义或导入的功能 
"""

"""
当一个模块文件中有__all__变量，当使用from xxx import *导入时，只能导入这个列表的元素
"""
from my_module1 import *
try:
    print(sum(12, 13))
except:
    print("找不到这个模块")
