# 继承:面向对象的继承指的是多个类之间的所属关系，即子类默认继承父类的所有属性和方法
# 所以类默认继承object类，object类是顶级类或基类，其他子类叫做派生类
# 当一个类有多个父类的时候,默认使用第一个父类的同名属性和方法
# 当一个子类和父类拥有同名的属性和方法,调用子类里面的同名属性和方法
# 当子类需要调用父类的同名方法和属性时用 父类.方法(self) 需要注意的是调用后会替换同名属性和方法
# 类.__mro__ 可以输出当前这个类的所以父类的层级关系
# super()可以快速调用上一层的属性和方法[名称一样的情况下]

"""
意思就是说，多个集成最前面优先同名方法，
子和父同名优先子,子需要调用父时,需要传入self，
且初始值会被改变，需要重新调用一次子的初始化[一调用就要重新赋值]
"""

class A(object):
    """object是顶级类"""

    def __init__(self):
        self.num = "这是A"

    def info_print(self):
        print(self.num)


class C(object):
    def __init__(self):
        self.num = "这是C"

    def info_print(self):
        print(self.num)


class B(A, C):
    """
    B会继承A的所以属性和方法
    当一个类有多个父类的时候,默认使用第一个父类的同名属性和方法
    """
    pass


# 单继承:某个类继承单个父类
# 多继承:某个类继承多个父类

class D(A, C):
    def __init__(self):
        self.num = "这是D"

    def info_print(self):
        """因为下面调用了父类替换了初始值,所以需要重新调用该函数的子类"""
        self.__init__()
        print(self.num)

    def A_info(self):
        """需要传入对象才能成功调用"""
        A.__init__(self)
        A.info_print(self)
        """如果修改了类名，这里也要修改，麻烦所以说可以使用super"""

    def C_info(self):
        C.__init__(self)
        C.info_print(self)


    def AA_info(self):
        """super(当前类名,self)"""
        super(D, self).__init__()
        super(D, self).info_print()
        """当然可以不添加参数"""

    def AAA_info(self):
        super().__init__()
        super().info_print()

result = B()
# 创建B
result.info_print()
# 调用B
result1 = D()
# 创建D
result1.info_print()
# 调用D
print(D.__mro__)
# 打印出其基础的父类
result1.A_info()
# 调用A的方法
result1.C_info()
# 调用C的方法
result1.info_print()
print("\n", end="\n")


class E(D):
    pass


result3 = E()
result3.info_print()
result3.AA_info()
result3.AAA_info()
# 允许继承到孙子


