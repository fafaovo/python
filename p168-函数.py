# 函数
"""
def 函数名(参数):
    代码
"""
# 定义函数
def info_print():
    """打印hello world"""
    print("hello world")
# 调用函数
# info_print()
# def add_num(a, b):
# # 此处ab为行参
#     return a + b
# print(add_num(int(input("请输入第一个:>")), int(input("请输入第二个:>"))))
# # 此处ab为实参

# 函数的说明文档
# help(函数名) 查看函数的说明文档
# 自定义函数的说明文档
"""
def 函数名(参数):
    """ "<-[不需要]说明文档的位置[不需要]->" """
    代码
"""
help(info_print)

# 打印一条斜杠
def print_line(a):
    """
    打印若干跳线
    :param a: -的数量
    :return: 无返回值
    """
    print('-' * a)
print_line(20)


# 求三个数的平均值
def print_add(a,b,c):
    return a+b+c
def print_mean(a,b,c):
    return print_add(a, b, c)/3

print("%.2f" %print_mean(14,25,62))

