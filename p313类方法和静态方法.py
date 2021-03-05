# 类方法:需要用装饰器@classmethod 来标识为类方法
# 第一个参数必须是类对象，一般以cls作为第一个参数
# 类方法一般用于访问私有属性时
class Dog(object):
    __tooth = 10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth

    def get_tooth1(self):
        return self.__tooth

wangcai = Dog()
result = wangcai.get_tooth()

print(result)
print(wangcai.get_tooth1())

# 静态方法 :不需要参数传递，减少内存消耗
# 静态方法就是不需要传递参数的方法
class Cat(object):
    @staticmethod
    def info_print():
        print("这是一只猫")


xiaomao = Cat()
xiaomao.info_print()
