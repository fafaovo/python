import os
import time
os.chdir("测试")
try:
    f = open('text.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(1)
            print(content, end="")
    except:
        print("意外终止了读取数据")
except:
    print("没有这个文件")