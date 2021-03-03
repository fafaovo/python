# 查找
"""
开始和结束位置下标则表示在整个字符串中查找
字符串序列.find(子串,开始位置下标,结束位置下标) 检测某个子串是否包含在这个字符串中，如果在返回下标不在返回-1
index和find一样，但是找不到会报错
rfind和rindex是从右向左找
count是返回出现次数
"""
mystr = "hello world and itcast and itheima and python"
if mystr.find("and") != -1:
    print("找到了")
if mystr.index("and") != -1:
    print("找到了")
print(mystr.count("and"))

# 修改
"""
replace(旧子串,新子串,替换次数)
替换:不写替换次数则全部替换,返回新子串,不修改原子串
"""
new_str = mystr.replace("and", "he")
print(new_str)
"""
split(分割字符,分割字符出现的次数)
分割:返回一个列表，丢失分割字符
"""
list1 = mystr.split("and")
print(list1)
"""
连接符.join(合并的列表)
合并:
"""
mylist = ['aa', 'bb', 'cc']
newlist = "...".join(mylist)
print(newlist)
"""
capitalize第一个字符转大写
title每个单词首字母转换成大写
lower大写转小写
upper小写转大写
"""

"""
strip删除字符串两侧空白字符
lstrip删除左侧
rstrip删除右侧
"""
"""
ljust 左对齐
rjust 右对齐
center 居中对齐
参数(在设置长度内进行对齐,替补填充字符)
"""
mystr = "haha"
print(mystr.center(20))
"""
isalpha如果字符串至少有一个字符并且所有字符都是字母返回true，否则false
isdigit如果字符串只包含数字返回true，否则返回false
isalnum至少有一个是字符，且是数字或者字母返回true，否则false
isspace只包含空白,则返回true,否则false
"""
# replace替换split分割join合并(r/l)strip删除两侧空白(r/l)just对齐
