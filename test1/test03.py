
import os
from PIL import Image
import shutil
import sys
image_size=144
#改变之后的图片尺寸

source_path=os.getcwd()+"/image/"#等待转换的图片存放地址
types='png' #转换后的图片格式
target_path=os.getcwd()+"/changepng/"#转换过格式的图片存放地址
final_path=os.getcwd()+"/final/"# 转换过格式和尺寸的图片存放地址

#如果没有转换后的图片存放文件夹，就创建对应的文件夹
if not os.path.exists(target_path):
    os.makedirs(target_path)
if not os.path.exists(final_path):
    os.makedirs(final_path)

def changepng(source_path,types):
    files = []
    image_list=os.listdir(source_path)
    #print(image_list)
    files = [os.path.join(source_path,_) for _ in image_list]
    for index,jpg in enumerate(files):
        if index > 1000:
            break
        try:
            sys.stdout.write('\r>>Converting image %d/100000 ' % (index))
            sys.stdout.flush()
            im = Image.open(jpg)
            png = os.path.splitext(jpg)[0] + "." + types
            im.save(png)
            shutil.move(png,target_path)
        except IOError as e:
            print('could not read:',jpg)
            print('error:',e)
            print('skip it\n')
    sys.stdout.write('Convert Over!\n')
    sys.stdout.flush()


if __name__ == '__main__':
    path = r"F:\untitled7\get_html\imgs"
    changepng(path, "png")
