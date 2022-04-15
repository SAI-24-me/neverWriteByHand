import random
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


def word2pic(txt_path='./test.txt', ttf_path="./src/test.TTF", save_path="./result/", size=4):
    font = ImageFont.truetype(ttf_path, 25)  # 设置字体
    f = open(txt_path, 'r', encoding='utf-8')  # 设置文档
    string = f.read()
    f.close()
    lenstr = len(string)
    page = 1
    flag = 0
    while flag < lenstr:
        img = Image.open('./src/background.png')
        draw = ImageDraw.Draw(img)
        for i in range(28):
            for j in range(38):
                if flag >= lenstr:
                    break
                if string[flag] == '\n':
                    flag += 1
                    break
                draw.text((70 + random.random() * size / 2 + 25 * j, 83 + random.random() * size + i * 48),
                          string[flag], (0, 0, 0),
                          font=font)
                flag += 1
            if flag >= lenstr:
                break
        img.save(save_path + str(page) + ".png")
        img.show()
        page += 1


if __name__ == "__main__":
    size = 4  # 整齐度
    txt_path = './test.txt'  # 文档位置
    ttf_path = "src/test.TTF"  # 字体位置
    save_path = "./result/"  # 储存文件夹 若没有不会自动生成
    word2pic(txt_path, ttf_path, save_path, size)
    print("success!")
