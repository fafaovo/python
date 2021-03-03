# 字典
dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}
# 'name[key]': 'TOM[对]' 是一个键值对
# 空字典
dict2 = {}
dict3 = dict()

# 字典修改数据或者新增数据
dict1['name'] = 'Rose'
dict1['id'] = 110
print(dict1)

# del删除 clear清空
# 查找 key值查找,找不到会报错
# 字典序列.get(key,默认值),如果找不到返回默认值,如果没写默认值返回None
# keys 查找字典里面所有的key 返回可迭代对象[可用for循环遍历]
# values查找字典里面所有值 返回可迭代对象
# items 查找字典里面所有的键值对 返回可迭代对象 元组
print(dict1.get('name'))
print(dict1.keys())
print(dict1.values())
print(dict1.items())
for item in dict1.items():
    print(f"key:{item[0]},values:{item[1]}", end=" ")
print("\n拆包写法")
for key, value in dict1.items():
    print(f"{key}={value}", end=" ")
print("\n")
