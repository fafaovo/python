import functools
# 高阶函数：把一个函数作为另外一个函数的参数传入
# abs() 绝对值 round() 四舍五入
print(abs(-10))
print(round(1.9))


# 任意两个数字，先求绝对值，在求和
def add_sum(a, b):
    return abs(a) + abs(b)


print(add_sum(12, -10))


def abs_sum(a, b, c):
    return c(a) + c(b)


print(abs_sum(12, -14, abs))
print(abs_sum(1.9, 1.4, round))
# 意思就是函数名可以作为参数传递

"""内置高阶函数"""
"""
  map(函数名,列表序列) 将传入的函数变量作用到 列表序列中每一个元素中
Python2将结果组成新的列表返回 Python3将返回迭代器
[map就是让列表中每一个元素都运行一次函数]
  reduce(函数名,列表序列) 每次函数执行后的结果继续和序列的下一个元素做累积计算
要想使用result需要导入import functools
[reduce就是让列表中每一个元素都运行一次函数,然后相加]
  filter(函数名,列表系列)过滤掉不符合条件的元素,返回一个filter对象
[reduce相当于if过滤]
"""
# 假设要计算list1里面各个数字的2次方
list1 = [1, 2, 3, 4, 5, 6]


def func(x):
    return x**2


result = map(func, list1)
print(result)
# 直接返回地址
print(list(result))
# 转换成列表即可得到结果


def func1(a, b):
    return a + b


result = functools.reduce(func1, list1)
print(result)


# 假设要过滤偶数
def func2(x):
    return x % 2 == 0


list2 = [i for i in range(1, 21)]
result = filter(func2, list2)
print(list(result))

