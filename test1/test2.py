import os
import re
import sys
import glob

path = r"F:\untitled7\get_html\imgs"
fileList = os.listdir(path)  # 待修改文件夹
print("修改前：" + str(fileList))  # 输出文件夹中包含的文件
os.chdir(path)  # 将当前工作目录修改为待修改文件夹的位置
imgs_path = "F:/untitled7/get_html/imgs"
pathname = imgs_path + "\*.png"
num = 0  # 名称变量
s = glob.glob(pathname=pathname)
for fileName in fileList:  # 遍历文件夹中所有文件
    url = s[num]
    img_name1 = url[url.rfind('imgs\\'):].replace('imgs\\', "")
    img_name3 = img_name1[0:img_name1.rfind('.png'):]
    img_name2 = img_name1[0:img_name1.rfind('.png'):]
    if "(" in img_name2:
        img_name2 = img_name2[0:img_name2.rfind('('):]
        print(img_name2)
    pat = ".+\.(jpg|jpeg|JPG)"  # 匹配文件名正则表达式
    pattern = re.findall(pat, fileName)  # 进行匹配
    print('pattern[0]:', pattern)
    os.rename(fileName, str(num) + ".png") # 文件重新命名
    num = num + 1  # 改变编号，继续下一项
print("---------------------------------------------------")
sys.stdin.flush()  # 刷新
print("修改后：" + str(os.listdir(path)))  # 输出修改后文件夹中包含的文件
