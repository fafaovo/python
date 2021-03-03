import os

# os.mkdir('测试')

os.chdir('测试')


for i in range(10):
    new_name = str(i)+".txt"
    f1 = open(new_name, 'w')
    f1.write("aaa")
    f1.close()

list1 = os.listdir()
for i in list1:
    os.rename(i, 'python_' + i)

"""
list1 = os.listdir()
for i in list1:
    os.remove(i)
"""
