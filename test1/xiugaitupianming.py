import os
import re
import sys

def update_img_name(path, imgName, num=1):
    fileList = os.listdir(path)  # 待修改文件夹
    if num != 1:
        num = 10000
    # print("修改前：" + str(fileList))  # 输出文件夹中包含的文件
    os.chdir(path)  # 将当前工作目录修改为待修改文件夹的位置
    for fileName in fileList:  # 遍历文件夹中所有文件
        pat = ".+\.(jpg|jpeg|JPG|png)"  # 匹配文件名正则表达式
        pattern = re.findall(pat, fileName)  # 进行匹
        # print(pattern)
        # print('num：', num, 'filename:', fileName)
        os.rename(fileName, (imgName + "(" + str(num) + ').' + pattern[0]))  # 文件重新命名
    #     num = num + 1  # 改变编号，继续下一项
        num += 1
    print("---------------------------------------------------")
    sys.stdin.flush()  # 刷新
    #print("修改后：" + str(os.listdir(path)))  # 输出修改后文件夹中包含的文件


if __name__ == '__main__':
    update_img_name(r"F:\untitled7\get_html\imgs", "艺术拼图", 1)