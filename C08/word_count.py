"""单词统计
统计练习项目的所有程序文件中不同单词的出现次数
"""
import os
import re
root = "../"
po = re.compile(r"\w+")  # 匹配任意单词的正则表达式


def main():
    pydir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(pydir)
    wdict = {}
    for folder, subfolders, files in os.walk(root):
        if folder.endswith("Temp"):
            continue
        for file in files:
            if file.endswith((".py", ".pyw")):
                with open(os.path.join(folder, file), encoding="utf-8") as f:
                    for line in f:
                        # 使用正则表达式将字符串拆分为单词并更新频度字典
                        for word in po.findall(line):  # 行拆分为单词
                            wdict.setdefault(word, 0)
                            wdict[word] += 1
    # 排序输出频度最高的50个单词
    result = sorted(wdict.items(), key=lambda i: i[1], reverse=True)
    cnt = 0
    for k, v in result[:50]:
        print(f"{k:>8} {v:3}", end=" ")
        if cnt % 5 == 4:
            print()
        cnt += 1


if __name__ == "__main__":
    main()
