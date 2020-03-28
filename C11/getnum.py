"""接受用户输入：使用try语句处理异常
"""


def main():
    ans = ""
    while True:
        ask = input("请输入一个数字或回车退出：")
        if ask == "":
            break
        try:
            # 断言字符串代表数字，断言为假时触发异常
            assert ask.replace(".", "", 1).isdigit(), "输入的不是数字"
            ans = eval(ask)
        except Exception as ex:
            ans = "错误：" + repr(ex)
        finally:
            print(ans)


if __name__ == "__main__":
    main()
