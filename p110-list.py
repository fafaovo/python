import random
"""
列表一个列表存储最好是相同类型
"""
list1 = ["replace", "split", "join", "strip", "just"]
str1 = "replace split join strip just"
"""
len(名)返回长度[公共操作]
index和count用法基本一致
"""
print(len(list1))
"""
判断指定数据是否在某个列表序列中[公共操作]
in 
not in

print("split" in list1)
print("split" in str1)
str = input("请输入要查找的字符串")
if str in list1:
    print(f"找到了!{str}在数组中底数为{list1.index(str)}")
else:
    print(f"找不到{str}")
"""


"""
添加内容
append列表增加到结尾  append追加数据的时候如果数据是一个序列，就会追加整个序列
extend列表追加 追加如果是应该序列,会拆开依次追加
insert(位置,数据) 指定位置追加 其他效果同 append
"""
list1.append("juele")
print(list1)
list1.append(["juele","liangle"])
list1.extend(["ljust","rjust"])
list1.insert(4, ["ljust","rjust"])
print(list1)
"""
删除内容
del 可以指定一个数据也可以指定下标删除
pop 指定下标或者删除最后一个数据，返回被删除的数据
remove 删除名字
clear 清空列表
"""
str2 = [1, 2, 3, 4, 5, 6]
# del str2[1]
print(str2)
"""
reverse 逆序
sort(reverse=布尔) 排序
"""
str2.reverse()
print(str2)
"""
copy 列表复制
"""
str3 = str2.copy()
print(str3)

list2 = []
class1 = []
class2 = []
class3 = []
effices = [[], [], []]
i = 0
while i < 8:
    strc1 = "cla"+str(i)
    list2.append(strc1)
    i += 1
print(list2)
for k in list2:
    num = random.randint(0, (len(effices)-1))
    effices[num].append(k)
list2.clear()
print(f"办公室{list2}")
print(effices)
for effice in effices:
    print(f"{effices.index(effice)}号办公室有{len(effice)}个人,他们分别是", end=" ")
    for cls in effice:
        print(f"{cls}", end=" ")
    print("")

# end=p127



