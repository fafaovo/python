from studentsys.student import *


class studentManager(object):
    def __init__(self):
        self.student_list = []
        pass

    def run(self):
        self.load_student()
        # 1.加载文件夹里面的学员数据
        while True:
            # 2. 显示功能菜单
            self.show_menu()
            # 3. 用户输入目标功能序列号
            try:
                menu_num = int(input("请输入您需要的功能序号:>"))
            except Exception as result:
                print(f"你的输入有误，错误代码{result}")
                continue
            else:
                # 4. 根据用户输入的序号执行不同的功能
                if menu_num == 1:
                    self.add_student()
                    # 添加学员
                    pass
                elif menu_num == 2:
                    self.del_student()
                    # 删除学员
                    pass
                elif menu_num == 3:
                    self.modify_student()
                    # 修改学员
                    pass
                elif menu_num == 4:
                    self.search_student()
                    # 查询学员
                    pass
                elif menu_num == 5:
                    self.show_student()
                    # 显示学员
                    pass
                elif menu_num == 6:
                    self.save_student()
                    # 保存学员
                    pass
                elif menu_num == 7:
                    # 退出系统
                    self.save_student()
                    break
                else:
                    print("重新输入")

    # 二.系统功能函数

    @staticmethod
    def show_menu():
        print("请选择如下功能")
        print("1.添加学员  2.删除学员  3.修改学员")
        print("4.查询学员  5.显示学员  6.保存学员")
        print("7.退出系统")

    def add_student(self):
        """添加学员"""
        name = input("请输入姓名")
        gender = input("请输入性别")
        tel = input("请输入手机号")
        stu = student(name=name, gender=gender, tel=tel)
        self.student_list.append(stu)
        pass

    def del_student(self):
        """删除学员"""
        del_name = input("请输入要删除学员的姓名:>")
        for i in self.student_list:
            if i.name == del_name:
                self.student_list.remove(i)
                print(f"删除{i.name}成功")
                break
        else:
            print("查无此人")

    pass

    def modify_student(self):
        """修改学员"""
        modify_name = input("请输入要修改学员的姓名:>")
        for i in self.student_list:
            if i.name == modify_name:
                gender = input("请重新输入性别")
                tel = input("请重新输入电话")
                i.gender = gender
                i.tel = tel
                print("修改成功")
        else:
            print("查无此人")

    def search_student(self):
        """查询学员"""
        search_name = input("请输入要查询的姓名")
        for i in self.student_list:
            if i.name == search_name:
                print("找到的信息如下")
                print(f"姓名是{i.name},性别是{i.gender},手机号是{i.tel}")
        else:
            print("查无此人")
        pass

    def show_student(self):
        """显示学员"""
        n = "姓名"
        g = "年龄"
        t = "电话"
        print("%-10s%-10s%-10s" % (n, g, t))
        for i in self.student_list:
            print("%-10s%-10s%-10s" % (i.name, i.gender, str(i.tel)))

    def save_student(self):
        """保存学员"""
        f = open("stu.date", "w")
        new_list = [i.__dict__ for i in self.student_list]
        # 遍历整个列表，取到每个i这个的对象，然后把他保存到__dict__里面，并且__dict__会自动生成一个对应的列表
        f.write(str(new_list))
        f.close()
        print("保存学员")

    def load_student(self):
        """加载学员"""
        try:
            f = open("stu.date", 'r')
        except:
            return
        else:
            data = f.read()
            new_list = eval(data)
            self.student_list = [student(i['name'], i['gender'], i['tel']) for i in new_list]
            f.close()

        # 此处思路是这样的，首先我们尝试去读取stu.date这个文件，不能打开就结束语句
        # 如果正常打开就会走到else里面，首先把读取到的放到data里面，此时应该是应该"[字典,字典]"的类型
        # eval()函数相当于去掉""，我们就得到一个列表[字典，字典]，然后我们去遍历整个列表，
        # 并且取到i字典，并且以键值对的形式调用学生对象，最终把结果存入学生列表中，关闭文件已结束
