# 推导式[生成式]:用一个表达式创建一个有规律的列表或者控制一个有规律的列表 [化简代码]
# 列表 字典 集合

list1 = []
i = 0
while i < 10:
    list1.append(i)
    i += 1
print(list1)

list1 = []
for i in range(10):
    list1.append(i)
print(list1)

# 使用推导式
list2 = [i for i in range(10)]
print(list2)
# 此处的i为for循环的返回值

# 假如说取偶数
list2 = [i for i in range(10) if i % 2 == 0]
print(list2)

list3 = []
for i in range(1, 3):
    for k in range(3):
        list3.append((i, k))
print(list3)
list3.clear()
list3 = [(i, k) for i in range(1, 3) for k in range(3)]
print(list3)
dict1 = {i: i**2 for i in range(1, 6)}
print(dict1)

# 字典推导式:
# 将两个合并
list1 = ['name', 'age', 'gender']
list2 = ['Tom', '20', 'man']
dict2 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict2)
# 提取数据
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
dict3 = {keys: value for keys, value in counts.items() if value >= 200}
print(dict3)

# 集合推导式:使用不多



