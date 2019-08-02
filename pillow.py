from PIL import Image, ImageFilter
im = Image.open('img/test.png')

def main ():
    # 画像サイズを取得
    print(im.format, im.size, im.mode)

if __name__ == "__main__" :
    main()