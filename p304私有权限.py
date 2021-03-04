# 私有属性:让方法不继承给子类
# 设置私有属性和方法:在属性或者方法名前面加上两个下划线_
# 一般定义函数名get_xx获取私有属性,定义set_xx来修改私有属性值[推荐写法]
# 私有方法只能通过类内部进行调用,获取和修改私有属性的方法未被私有所以可以被子类调用


class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'
        self.__money = 10000

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

    def __fanfa(self):
        print("这是一个私有方法")

    def get_money(self):
        """获取私有属性,没有__所以会继承给子类"""
        return self.__money

    def get_fanfa(self):
        self.__fanfa()

    def set_money(self):
        """修改私有属性"""
        self.__money = 5000


class Prentice(Master):
    pass


daqiu = Prentice()
daqiu.make_cake()
# 子无法访问到其父的钱
# use1.__money()
xiaoqiu = Prentice()
print(daqiu.get_money())
print(xiaoqiu.get_money())
daqiu.set_money()
print(daqiu.get_money())
daqiu.get_fanfa()
xiaoqiu.get_fanfa()

