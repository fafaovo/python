import my_package.my_module as mm
import my_package.my_module1
# 导入:包名.模块名

# 包就是一个文件夹，包里面存储这很多有联系的文件
# 包内会自动创建_init_文件，可以控制包的导入行为
# 在这个文件可以用_init_控制允许导入的模块列表
# 如果想使用form 包名 import * 来导入模块，必须使用_init_来设置

mm.info_print0()
my_package.my_module1.info_print0()