"""
运算符       描述             支持类型
  +         合并             字符串,列表,元组
  *         复制             字符串,列表,元组
in[not in]  元素是否[不]存在   字符串,列表,元组,字典
"""
set1 = [10, 20]
print("_"*10)
print(set1*5)
print(10 in set1)
"""
len元素个数 del删除 max容器中元素最大值 min容器中元素最小值
range(start,end,step)生成从start到end的数字,步长为step,供for循环使用
enumerate(可编译对象,用于设置变量数据下标的初始值默认0)
用于将可编译的数据对象组合为一个缩影序列，同上列出数据和数据下标,一般用于for循环使用
"""
for i in range(10):
    print(i, end=" ")
print("")
for k in range(0, 10, 2):
    print(k, end=" ")
print("")
# range生成的序列不包含end数字,而且都是左闭右开,0要10不要
set2 = []
for i in range(11):
    set2.append(i)
print(set2)

list1 = ['a', 'b', 'c', 'd', 'e']
for i in enumerate(list1, start=0):
    print(i, end=" ")
# 可以用两个变量接收
