import os
# 操作文件和文件夹需要使用os模块
"""
os.rename(目标文件,新名字) 重命名文件/文件夹
os.remove(目标文件名) 删除文件/文件夹
"""
# os.rename('index\\object1[备份].txt', 'index\\10.txt')
# os.remove('index\\10.txt')

"""
os.mkdir(文件夹名字)创建文件夹
os.rmdir(文件夹名字)删除文件夹
os.getcwd()获取当前目录
os.chdir(目录)改变默认目录
os.listdir(目录)获取目录列表
"""
# os.mkdir('calls')
# os.rmdir('calls')

os.chdir('index\\')
print(os.getcwd())
print(os.listdir("..\\"))
