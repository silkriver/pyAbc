"""带有异常处理的命令行计算器
"""


def main():
    ans = ""
    while True:
        ask = input("输入算式或回车退出：")
        if ask == "":
            break
        try:
            ans = eval(ask)
        except Exception as ex:  # 捕获抛出的异常
            ans = repr(ex)
        print(ans)


if __name__ == "__main__":
    main()
