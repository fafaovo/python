"""
需求:学员储存在文件中
系统功能:增删查改
"""
from studentsys.student import *
from studentsys.System import *
# 导入模块
if __name__ == '__main__':
    """这个变量，决定在引入的时候是否要运行该文件"""
    student_manager = studentManager()
    student_manager.run()
