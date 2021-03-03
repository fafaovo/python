# 面向对象:类和对象[关系:用类去实例化[创建]一个对象]
"""
定义类
class 类名():
    代码

创造对象
对象名 = 类名()

"""


class Washer():
    """self等同于this"""

    def wash(self):
        """这个方法称为实例方法或者对象方法"""
        print("能洗衣服")
        print(self)


haier = Washer()
print(haier)
haier.wash()

# self指的是调用该函数的对象

# 添加和获取对象属性
# 在类的外面添加和获取的语法 对象名。属性名 = 值
haier.width = 500
haier.height = 800
print(f"haier洗衣机的宽度是{haier.width},高度是{haier.height}")


# 定义类
class Washer1():
    def __init__(self):
        """初始化对象 """
        self.width = 100
        self.height = 200

    def print_info(self):
        print(f"洗衣机的宽度是{self.width}")
        print(f"洗衣机的高度是{self.height}")


# 创建对象
haier1 = Washer1()
# 添加实例属性
haier1.width = 500
haier1.height = 800


# 魔法方法:__xx__()的函数算魔法方式,指的是具有特殊功能的函数
# _init_() 初始化对象[默认自动调用 ]
# _str_() 当打印对象默认输出对象地址,如果定义_str_方法，那么输出这个方法return的数值
# _del_() 当删除对象时,python解释和会默认调用,解释器结束时也会调用
haier1.print_info()
haier2 = Washer1()
haier2.print_info()
# 带参数的init
class Washer2():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "这是调用该对象输出的东西"

    def __del__(self):
        print(f"{self}对象已被删除")

    def print_info(self):
        print(f"洗衣机的高度是{self.height}")
        print(f"洗衣机的宽度是{self.width}")

haier3 = Washer2(100, 200)
haier3.print_info()
print(haier3)