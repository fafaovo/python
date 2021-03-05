# 自定义异常 raise 抛出异常
# 当ralse抛出异常，此时才能被Exception捕获
"""
需求:密码长度不足则报错
"""


class InputError(Exception):
    """自定义异常类"""

    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    def __str__(self):
        return f"你输入的长度是{self.length},不能少于{self.min_len}个字符"


try:
    con = input("请输入用户名")
    if len(con) < 3:
        raise InputError(len(con), 3)
    """当ralse抛出异常，此时才能被Exception捕获"""
except Exception as str1:
    print(str1)
else:
    print("输入完成")
