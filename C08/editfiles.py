"""编辑指定目录中的程序文件，在第一行注释文件名
"""
import os


def main():
    # 将程序文件所在目录设为当前工作目录
    pydir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(pydir)
    # 遍历当前目录的Temp子目录
    for folder, subfolders, files in os.walk("Temp"):
        for file in files:
            # 将目录名和文件名组合为文件路径
            path = os.path.join(folder, file)
            print(f"编辑文件：{path}")
            # 以读写模式打开文件
            with open(path, "r+", encoding="utf-8") as f:
                text = f.read()                 # 读入原有文本
                f.seek(0)                       # 读写位置回到文件开头
                f.write(f"# {file}\n" + text)   # 写入包含新注释行的文本


if __name__ == '__main__':
    main()
