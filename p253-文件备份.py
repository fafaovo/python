# 文件备份
old_name = "index\\"+input("请输入备份的文件夹")
index = old_name.rfind(".")

if index > 0:
    postfix = old_name[index:]

# rfind提取后缀点下标，从右开始找
# 组织新名字使用切片
new_name = old_name[:index]+'[备份]'+postfix
f1 = open(old_name, 'rb')
f2 = open(new_name, 'wb')
# 如果不确定目标文件大小，则循环写入,当读取的数据没有终止循环
while True:
    con = f1.read(1024)
    # 每次读取1024个，当读取不到时跳出循环
    if len(con) == 0:
        print("读取完成")
        break
    f2.write(con)
f1.close()
f2.close()
