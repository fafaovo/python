"""
封装:
    1.将数学和方法书写到类的里面的操作即为封装
    2.封装可以为属性和方法添加私有权限
继承:
    1.子类默认继承父类的所有属性和方法
    2.子类可以重写父类顺序和方法
多态:
    1.传入不同的对象,产生不同的结果
"""


# 多态:一类事物的多种形态(一个抽象类有多个子类，因而多态的概念依赖于继承)


class Dog(object):
    def work(self):
        """父类提供统一的方法,纳米是空方法"""
        print("指哪打哪")


class ArmyDog(Dog):
    def work(self):
        print("追击敌人")


class DrugDog(Dog):
    def work(self):
        print("追查毒品")


class Person(object):
    def work_with_dog(self, dog):
        dog.work()


ad = ArmyDog()
dd = DrugDog()

daqiu = Person()
daqiu.work_with_dog(ad)
daqiu.work_with_dog(dd)
# 就是搬家里面的item
# 意思就是说把对象作为实参传入函数叫做多态
