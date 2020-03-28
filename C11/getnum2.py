"""接受用户输入：使用if语句避免异常
"""


def main():
    ans = ""
    while True:
        ask = input("请输入一个数字或回车退出：")
        if ask == "":
            break
        elif ask.replace(".", "", 1).isdigit():  # 字符串是否代表数字
            ans = eval(ask)
        else:
            ans = "输入无效！"
        print(ans)


if __name__ == "__main__":
    main()
