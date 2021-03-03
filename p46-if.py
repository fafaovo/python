import random
"""
if 条件:
    执行代码1
    执行代码2
    ......

num1 = 1
num2 = 2
if num1 < num2:
    print("这个代码会执行")
    print("这个代码也会执行")

print("这个代码会执行")
联系 年龄大于等于18 输出 已经成年可以上网
"""

"""
age = int(input("请输入你的年龄:>"))
if (age >= 18) and (age <= 60):
    # 此处可以简化为 18 <= age <= 60
    print("你已满18，可以参加工作")
elif age < 18:
    print("未满十八岁")
elif age > 60:
    print("大于六十岁")
"""

"""
坐公交车 有钱可以上车 没钱不能上车 上车了有空座则可以坐下，没空座就要站着

# if嵌套
money = 1
seat = 1
if money == 1:
    print(f"你上车了,你有{money}块钱")
    if seat == 1:
        print("有座位")
    else:
        print("没有座位")
else:
    print("你没钱")
"""

Player = int(input("请出拳,0--石头,1--剪刀,2--布:>"))
computer = random.randint(0, 2)
if ((Player == 0) and (computer == 1)) or \
        ((Player == 1) and (computer == 2)) \
        or ((Player == 2) and (computer == 0)):
    print("玩家获胜")
elif Player == computer:
    print("平局")
else:
    print("电脑获胜")

"""
三目运算符
条件成立执行的表达式 if 条件 else 条件不成立执行的表达式
"""
num1 = int(input("变量1"))
num2 = int(input("变量2"))
print(f"{num1}-{num2}={num1 - num2}") if num1 > num2 else print(f"{num2}-{num1}={num2 - num1}")
a = random.randint(1, 100)
b = random.randint(1, 100)
c = a if a > b else b
print("%d %d %d" % (a, b, c))
