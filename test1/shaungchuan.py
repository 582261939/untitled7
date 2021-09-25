
from add_goods import *

types = "jpg"
imgs_path = "F:/untitled7/get_html/imgs"
pathname = imgs_path + "\*.{}".format(types)
s = glob.glob(pathname=pathname)
print(s)
imgs_size = len(glob.glob(pathname=pathname))
token = get_token()
slen = len(s)


for i in range(slen):
    url = s[i]
    img_name1 = url[url.rfind('imgs\\'):].replace('imgs\\', "")
    img_name3 = img_name1[0:img_name1.rfind('.{}'.format(types)):]
    img_name2 = img_name1[0:img_name1.rfind('.{}'.format(types)):]
    if "(" in img_name2:
        img_name2 = img_name2[0:img_name2.rfind('('):]
        print(img_name2)
    md5 = up_img(token, img_name3, types)
    add_goods(token, md5, img_name2)
    print(img_name2)