import random
"""
循环
"""
i = 0
while i < 5:
    print("好吧(╯▽╰)", end="")
    i += 1
print("结束")
i = 1
Sum = 0
while i <= 100:
    if i % 2 == 0:
        Sum += i
        print(i, end=" ")
    i += 1
print(f"\n{Sum}")

# 满足一定条件退出循环
# break--直接退出循环 continue--退出本次循环，执行下一次循环
i = 1
while i < 100:
    if i == random.randint(1, 10):
        print(f"\n你吃到虫子了,所以第{i}个苹果扔了")
        i += 1
        continue
    elif i >= 10:
        print("你吃饱了")
        break
    else:
        print(f"你吃到第{i}个苹果", end=" ")
        i += 1
i = 0
while i < 9:
    k = 0
    i += 1
    while k < i:
        k += 1
        print(f" {i}x{k}={i*k}", end="\t")
    print("")


"""
for 临时变量 in 序列:
    代码
"""
Str = "hello world!"
for i in Str:
    if i == "r":
        continue
    print(f"{i}", end="")


"""
while...else 此处的else需要循环正常结束之后才能执行
for...else 同理
"""
i = 0
while i <= 5:
    print(f"这是第{i}次", end=" ")
    i += 1
    if i == 5:
        print("跳出")
        continue
else:
    print("执行了吗？")
"""
如果循环体遇到break跳出循环，则不会执行else里面的语句
而遇到continue则依然会执行else里面的语句
"""



"""
a = 0
b = 0
while not((a == 3) or (b == 3)):
    Player = int(input("请出拳,0--石头,1--剪刀,2--布 :>"))
    computer = random.randint(0, 2)
    if ((Player == 0) and (computer == 1)) or \
            ((Player == 1) and (computer == 2)) \
            or ((Player == 2) and (computer == 0)):
        print("玩家获胜")
        a += 1
    elif Player == computer:
        print("平局")
    else:
        print("电脑获胜")
        b += 1
if a == 3:
    print("游戏结束,玩家胜利")
else:
    print("游戏结束,电脑胜利")
"""



