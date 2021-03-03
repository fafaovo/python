# 元组:可以存储多个数据,但是不能修改
tuple1 = (10, 20, 30)
print(tuple1)
tuple2 = (19,)
# 使用元组存储单个要在后面添加一个逗号
# 下标 index count len [通用方法]
# 元组中有列表,这个列表是可以修改的,一个列表里面有个元组,里面的元组不可修改
tl1 = list(tuple1)
tl1[0] = 30
tuple1 = tuple(tl1)
print(tuple1)
# 如果需求修改元组可以把他转换成列表进行修改

