n = int(input("计算1累加至n，请输入n："))  # 将输入内容转为整数，赋值给变量n
x = 1            # 变量x赋值1
result = 0       # 变量result赋值0
while x <= n:    # 当x小于等于n时循环执行子语句
    result += x  # result原值加x
    x += 1       # x原值加1
print(f"1累加至{n}的结果是{result}。")  # 输出包含n和result值的字符串
