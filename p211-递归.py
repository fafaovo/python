# 递归
# 需求N以内的数字累加和1+2+3...+N


def user_add(num):
    if num == 1:
        return 1
    return num + user_add(num - 1)


print(user_add(3))
