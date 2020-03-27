"""生成颜色元组并保存到文件
"""


def main():
    colors = []
    with open("rgb.txt") as file:
        for line in file:
            # 空行或!打头的行则不必处理
            if not (line.isspace() or line.startswith("!")):
                # 最后一个制表符之后的字符串 split("\t")[-1]
                # 再去掉末尾的换行符 [:-1] 就是颜色名
                # 把颜色名添加进列表即可
                colors.append(line.split("\t")[-1][:-1])
    for i in colors[:]:
        # 移除带有空格及英式拼法的颜色名
        if " " in i or "grey" in i.lower():
            colors.remove(i)
    with open("colorsinfo.py", "w") as file:
        # 生成颜色元组并保存到文件
        file.write("COLORS = "+str(tuple(colors)))


if __name__ == "__main__":
    main()
