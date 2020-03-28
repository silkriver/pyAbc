"""带有异常处理的命令行计算器2：多个except子句
"""


def main():
    ans = ""
    while True:
        ask = input("输入算式或回车退出：")
        if ask == "":
            break
        try:
            ans = eval(ask)
        except SyntaxError:         # 处理语法错误
            ans = "语法不正确"
        except ZeroDivisionError:   # 处理除零错误
            ans = "除数不能为零"
        except Exception as ex:     # 处理其他错误
            ans = repr(ex)
        finally:
            print(ans)


if __name__ == "__main__":
    main()
