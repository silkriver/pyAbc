s = input("请输入一个整数：")
i = int(s)
sign = 1              # 此变量值为1或-1，用来控制结果的正负
if i < 0: sign = -1   # 如果i为负数则sign赋值为-1
s = s.lstrip("-+")    # 去掉原字符串左侧的正负号
r = s[::-1]           # 反转字符串
result = sign*int(r)  # 令结果的正负性与输入值一致
print(result)
