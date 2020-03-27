def change(n):
    """改变全局变量的函数"""
    global total
    total += n
    print("总量 + 2 =", total)


total = 10
print("总量 =", total)
for i in range(1, 6):
    change(2)
