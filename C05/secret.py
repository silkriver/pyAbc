"""文本加密工具
加密 python secret.py -e 5 plain.txt cipher.txt
解密 python secret.py -d 5 cipher.txt plain.txt
"""
import sys


def enc(offset, text):
    """加密文本
    """
    newtext = ""
    for c in text:  # 每个字符码位值加移位数得到新的字符
        newtext += chr(ord(c) + offset)
    return newtext


def dec(offset, text):
    """解密文本
    """
    newtext = ""
    for c in text:  # 每个字符码位值减移位数得到新的字符
        newtext += chr(ord(c) - offset)
    return newtext


def main():
    """主函数
    """
    act = sys.argv[1]           # 加密/解密选项
    offset = int(sys.argv[2])   # 移位值
    fromfile = sys.argv[3]      # 原文件
    tofile = sys.argv[4]        # 目标文件
    with open(fromfile) as ff, open(tofile, "w") as tf:
        for line in ff:
            if act == "-e":     # 加密
                newline = enc(offset, line)
            elif act == "-d":   # 解密
                newline = dec(offset, line)
            tf.write(newline)


if __name__ == "__main__":
    main()
