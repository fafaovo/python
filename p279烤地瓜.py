# 烤地瓜
class SweetPotato():
    def __init__(self):
        """烤制时间 烤制状态 添加的调料"""
        self.cook_time = 0
        self.cook_static = '生的'
        self.condiments = []
        pass

    def __str__(self):
        """用于存储和对象的信息，便携输出"""
        return f"你的土豆烤制时间是{self.cook_time},状态是{self.cook_static},调料有{self.condiments}"
        pass

    def cook(self, time):
        """烤地瓜的时间应该用整体时间"""
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_static = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_static = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_static = '熟了'
        elif 8 <= self.cook_time < 10:
            self.cook_static = '熟透了'
        elif self.cook_time >= 10:
            self.cook_static = '烤糊了'
        pass

    def con(self, Seasoning):
        """添加调料"""
        self.condiments.append(Seasoning)


Potato1 = SweetPotato()
print(Potato1)
Potato1.cook(3)
print(Potato1)
Potato1.cook(3)
print(Potato1)
Potato1.cook(3)
Potato1.con("番茄酱")
Potato1.con("盐")
Potato1.con("糖")
Potato1.con("烤地瓜")
print(Potato1)
Potato1.cook(3)
print(Potato1)
