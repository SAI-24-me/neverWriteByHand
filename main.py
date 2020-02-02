import PIL, random , sys
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def main():
    lenstr = len(string)
    page = 1
    flag = 0
    while flag < lenstr:
        img = Image.open('text.png')
        draw = ImageDraw.Draw(img)
        for i in range(28):
            for j in range(38):
                if flag >= lenstr:
                    break
                if string[flag] == '\n':
                    flag += 1
                    break
                draw.text((70 + random.random() * size/2  + 25 * j, 83 + random.random() * size + i * 48), string[flag], (0, 0, 0),
                          font=font)
                flag += 1
            if flag >= lenstr:
                break
        img.save(str(page) + ".png")
        img.show()
        page += 1

if __name__ == "__main__":
    size = 4 #整齐度
    font = ImageFont.truetype("test.ttf", 25) #设置字体
    f = open(sys.argv[1], 'r', encoding='utf-8') #设置文档
    string = f.read()
    f.close()
    main()
    print("success!")
