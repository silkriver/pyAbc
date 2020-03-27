"""根据Base64编码的数据生成图片文件
"""
import base64
# 使用Base64编码的GIF格式图像数据
logo = """R0lGODlhIAAgAMQAAAAAAHt7ezMzM8TExKamplpaWhAQEN7e3
klJSYqKimpqaiEhIb29vUJCQuXl5czMzAgICJmZmbW1tTo6OoSEhBkZGe/v
75SUlCoqKnNzc9XV1WZmZlFRUa2trf///wAAACH5BAEHAB4ALAAAAAAgACA
AAAX/oCeOZGmeaCpaluqSFhNwAoZNXDK8p5UsgKBwKIjwRhLgcDmcPHgBpn
QIMaoUAMPEMB1WJsFEihI0OhKQaSXSygQJJ0YQchgNch0Go0MpOEZyWXUlS
gZ/Rx4DQgglF0MSiB6OQgwkGENWR5NBjCKKQhyRIg1CdCJkQk+iEkNwHhxC
AqIrFUIZHhYCQgWzImBBoQ6XQbe9CEINHsJCCr0epEETuMMA0rMWSgDJHr8
ApqKBQbweBUPjkd0AFCKbQReRWEOVHhpMGS0uDuVe+M9ZfEEWUHjQb4SFAR
m4LGkGSJwHVsxMwJLybcTEAB7QBMFYYh8TjiQc1DJE78KFQSQ8Ow7BgIJBm
gYFTagMUkFDig5pBErooCrlkgo9UQzIpk5mE5QqLChIA0BMxyAG1kXSkKGB
zRIMGlA4dCIEADs="""


def main():
    b = base64.b64decode(logo)          # 解码数据得到字节串
    with open("logo.gif", "wb") as f:   # 创建文件并写入字节串
        f.write(b)


if __name__ == '__main__':
    main()
