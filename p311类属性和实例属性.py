# 类属性和实例属性
# 实例属性:描述某个事物的特征,归属者是实力即对象
# 类属性:类对象所拥有的属性,归属者是类
"""类属性的优点"""
"""
记录某项数据始终保持一致时，可以定义类属性
实例属性要求每个对象都开辟一份内存空间
而类属性为全类所共有，只占用一份内存
节省内存空间
"""
"""
类属性只能通过类对象修改
不能通过对象修改属性，如果这样操作，实则创建了个实例属性
"""
class Dog(object):
    """这就是在设置类属性"""
    tooth = 10


wangcai = Dog()
xiaohei = Dog()
"""访问类属性"""
print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)
