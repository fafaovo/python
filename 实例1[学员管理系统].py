# 函数加强
"""学员管理系统"""


def menu():
    """菜单栏"""
    print("============================")
    print("====1.添加学员\t2.删除学员====")
    print("====3.修改学员\t4.查询学员====")
    print("====5.显示学员\t0.退出系统====")
    print("============================")


def user_add():
    """添加学生"""
    new_name = input("请输入要添加学员的名字:>")
    global info
    for i in info:
        if new_name == i['name']:
            print("该用户已经存在")
            return
    stu = {'name': new_name, 'age': input("请输入学生年龄:>"),
           'gender': input("请输入学生性别:>")}
    info.append(stu)
    print(info)
    pass


def user_del():
    """删除学生"""
    new_name = input("请输入要删除学员的名字:>")
    global info
    for i in info:
        if new_name == i['name']:
            info.remove(i)
            break
    else:
        print("你输入的学员不存在")
        return
    print(info)
    print("删除成功")
    pass


def user_modify():
    new_name = input("请输入要修改学员的名字:>")
    global info
    for i in info:
        if new_name == i['name']:
            i['name'] = input('请输入要修改的名字:>')
            i['age'] = input('请输入要修改的年龄:>')
            i['gender'] = input('请输入要修改的性别:>')
            print("修改完成")
            break
    else:
        print('没有找到该学员')
        return
    print(info)
    pass


def user_query():
    """查询"""
    new_name = input("请输入你要查询人的名字:>")
    global info
    for i in info:
        if i['name'] == new_name:
            print("查询到学员信息如下:----------")
            print(f"该学员的名字是{i['name']},年龄是{i['age']},性别是{i['gender']}")
            break
    else:
        print("没有查询到该成员")
        return
    pass


def user_display():
    """打印"""
    global info
    print("姓名\t年龄\t性别")
    for i in info:
        print(f"{i['name']}\t{i['age']}\t{i['gender']}")
    pass


def user_beifen():
    global info
    f1 = open("index\\object1.txt", 'w')
    for i in info:
        f1.write(i['name']+"\t")
        f1.write(i['age']+"\t")
        f1.write(i['gender']+"\t")
        f1.write("\n")
    f1.close()
    pass



def user_white():
    global info
    f1 = open("index\\object1.txt", 'r')
    while True:
        con = f1.readline()
        if len(con) == 0:
            break
        list1 = con.split("\t")
        del list1[len(list1)-1]
        stu = {"name": list1[0], "age": list1[1], "gender": list1[2]}
        info.append(stu)
    f1.close()
    pass


put = 1
# stu = {"name": "", "age": "", "gender": ""}
info = []
user_white()
while put:
    menu()
    put = input("请选择:>")
    if put.isdigit():
        put = int(put)
    else:
        print("你输入的有误")
        continue
    if put == 1:
        user_add()
    elif put == 2:
        user_del()
    elif put == 3:
        user_modify()
    elif put == 4:
        user_query()
    elif put == 5:
        user_display()
    elif put == 0:
        user_beifen()
        break
    else:
        print("你输入的有误请重新输入")
        continue
