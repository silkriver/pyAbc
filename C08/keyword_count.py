"""关键字统计
统计练习项目的所有程序文件中Python保留关键字的出现次数
"""
import os
from string import punctuation as punc
from keyword import kwlist
root = "../"    # 遍历起点设为程序文件所在目录的上级目录即练习项目的主目录


def main():
    pydir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(pydir)
    kwdict = dict(zip(kwlist, [0] * len(kwlist)))       # 初始化关键字频度字典
    for folder, subfolders, files in os.walk(root):     # 遍历练习项目主目录
        if folder.endswith("Temp"):
            continue
        for file in files:
            if file.endswith((".py", ".pyw")):
                with open(os.path.join(folder, file), encoding="utf-8") as f:
                    for line in f:
                        # 创建转换对照表，将所有标点符号替换为空格
                        table = str.maketrans(punc, " " * len(punc))
                        line = line.translate(table)
                        for word in line.split():   # 文本拆分为单词
                            if word in kwlist:      # 如为关键字则更新结果字典
                                kwdict[word] += 1
    # 排序输出关键字频度
    result = sorted(kwdict.items(), key=lambda i: i[1], reverse=True)
    cnt = 0
    for k, v in result:
        print(f"{k:>8} {v:3}", end=" ")
        if cnt % 5 == 4:
            print()
        cnt += 1


if __name__ == "__main__":
    main()
