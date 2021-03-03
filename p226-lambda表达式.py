# lambda[匿名函数]表达式：如果一个函数有一个返回值,并且只有一句代码，可以使用lambda简化
"""
语法: lambda 参数列表 : 表达式
lambda表达式的参数可有可无,函数的参数在表达式中完全适用
lambda表达式能接受任何形式的参数，但是只能返回一个值
"""


def fn1():
    return 200


fn2 = lambda: 100
print(fn2)
# 直接打印表达式,返回内存地址
print(fn2())

# lambda 参数:返回值兼表达式
fn3 = lambda a, b: a + b
print(fn3(2, 114))

# lambda 参数可以使用默认参数 可变参数[*args]和[**kwargs]
fn4 = lambda a, b, c=100: a + b + c
print(fn4(10, 20))

fn5 = lambda *args: args
print(fn5('xiaoming', 'xiaoli'))

fn5 = lambda **kwargs: kwargs
print(fn5(name='xiaoli', age=12))

# 带判断的lambda
fn6 = lambda a, b: a if a > b else b
# 三元表达式
print(fn6(500, 100))

# 列表数据按字典key的值排序
students = [
    {'name': 'TOM', 'age': 12},
    {'name': 'ROSE', 'age': 19},
    {'name': 'Jack', 'age': 22}
]
students.sort(key=lambda x: x['name'], reverse=True)
print(students)
