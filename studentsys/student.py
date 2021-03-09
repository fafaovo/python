class student(object):
    """1，首先要定义学生这个类"""
    def __init__(self, name, gender, tel):
        """我们假设学生这个类需要姓名 性别和电话"""
        self.name = name
        self.gender = gender
        self.tel = tel
        pass

    def __str__(self):
        return f'{self.name},{self.gender},{self.tel}'
        pass

    # __dict__ 收集类对象或者实力对象的实例和方法,返回一个字典



