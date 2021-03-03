# 集合:有去重效果
# 创建空集合只能用set(),因为{}用来创建字典了
set1 = {10, 20}
# 增加数据 add()增加单一数据 update()增加序列
set1.add(30)
set1.add(10)
print(set1)
set1.update([10, 20, 30, 40, 50])
print(set1)
"""
删除数据 
 remove 删除指定数据，不存在会报错 
 discard 删除指定数据，不存在不会报错
 pop 随机删除,并且返回
"""
# 查找 使用in语法
print(10 in set1)
print(10 not in set1)
