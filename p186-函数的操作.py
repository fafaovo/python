# 如果想在函数体内修改全局变量,需要使用global关键字声明
a = 100
def testA():
    print(a)
def testB():
    global a
    a = 200
testA()
testB()
testA()

# python允许多个返回值
def return_num():
    return 1, 2
num1, num2 = return_num()
print(f"返回{num1}和{num2}")

"""
函数的参数
1.位置参数:调用函数时根据函数定义的参数位置来传递参数
2.关键字参数:键=值来指定
3.缺省参数:默认参数，用于定义函数为参数提供默认值，调用时可不传该默认阐述
4.不定长参数:可变参数，用于不确定的时候会传递多少个参数,此时可以用包裹(packing)位置参数,或者包裹关键字参数，来进行参数传递
不定长参数分为 包裹位置传递 包裹关键字传递
"""
def user_info(name, age, gender):
    print(f"名字:{name},年龄:{age},性别:{gender}")
# 1.位置参数
user_info('tom',20,'男')
# 2.关键字参数:函数调用时，如有位置参数，位置参数需写在关键字参数前面
user_info(gender='男', name='小明', age='16')
# 3.缺省参数:函数调用时,如果为缺省参数传值则修改参数值
def user_lack(name,age,gender='男'):
    print(f"名字:{name},年龄:{age},性别:{gender}")
user_lack('小李',15)
# 4.不定长参数-包裹位置：他们会合并为一个元组
def user_Indefinite(*args):
    print(args)

user_Indefinite('TOM',18 ,'男')
# 包裹关键字传递：打包返回字典
def user_oin(**kwargs):
    print(kwargs)
user_oin(name='TOM',age=18,id=110)

# 对字典进行拆包时，其实取出来的是字典的key
dict1 = {'name': 'TOM', 'age': 18}
b, c = dict1
print(b)
print(c)
print(dict1[b])
print(dict1[c])


