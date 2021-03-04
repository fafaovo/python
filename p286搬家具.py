# 搬家具
class Furniture():
    def __init__(self, name, area):
        """家具名字 家具占地面积"""
        self.name = name
        self.area = area


class host():
    def __init__(self, position, area):
        """房屋位置 房屋大小 放入家具后大小 家具列表"""
        self.Position = position
        self.AllArea = area
        self.NowArea = area
        self.list = []

    def place(self, item):
        if self.NowArea < item.area:
            print(f"你的房子放不下{item.name}")
        else:
            self.NowArea -= item.area
            self.list.append(item.name)

    def __str__(self):
        return f"你的房子在{self.Position},占地面积{self.AllArea},余剩面积{self.NowArea},家具列表{self.list}"


NewHost = host("北京", 150)
# 房屋位置 房屋大小
dest = Furniture("桌子", 10)
dest1 = Furniture("大桌子", 20)
dest2 = Furniture("超大的桌子", 100)
NewHost.place(dest)
NewHost.place(dest1)
print(NewHost)
NewHost.place(dest2)
print(NewHost)
