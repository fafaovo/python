a = "hello " \
    "world"
a1 = 'hello world'
b = '''i am 
TOM'''
b1 = """i am TOM"""
print(type(b))
# 三引号支持回车换行


# 切片
str1 = "abcdefg"
# 假如说我要拿到cde三个字符，那么就需要用到切片了
# 序列[开始位置下标:结束位置下标:步长] 步长是选取间隔,默认1,开始会截入,结束不会截入
# 开始不写默认从0开始,结束不写表示选取到最后,都不写则从头选到位
# 步长是负数表示倒序，开始结束是负数则是从最后一个数据依次向前推进
print(str1[2:5:1])
str2 = "012345678"
print(str2[-4:-1:1])
print(str2[-4:-1:-1])# 无结果
# 如果选取方向和步长方向冲突，则无法选取到数据
