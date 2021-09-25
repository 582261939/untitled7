import requests
import json
import glob


def get_token():
    url = "http://erp.fjlonfenner.com/uaa/oauth/token"
    data = {
        "username": "zhangzhenwei",
        "password": "zzy1472580",
        "rememberMe": "true",
        "grant_type": "password"
    }
    headers = {
        "Authorization": "Basic d2ViX2FwcDo=",
        "Accept-Encoding": "gzip, deflate"
    }
    s = requests.post(url=url, data=data, headers=headers).content
    token = json.loads(s)["access_token"]
    return token


def up_img(token, img_name, types):
    url2 = "http://erp.fjlonfenner.com/image/api/image/upload"
    cookie = "crx_token=" + token
    Authorization = "Bearer " + token
    headers1 = {
        "Cookie": cookie,
        "Authorization": Authorization
    }
    # F:\untitled7\get_html\imgs
    img_path = r'F:\untitled7\get_html\imgs/' + str(img_name) + ".{}".format(types)

    files = {'file': (str(img_name) + '.{}'.format(types), open(img_path, 'rb'), 'image/{}'.format(types))}

    r2 = requests.post(url=url2, headers=headers1, files=files).content
    md5 = json.loads(r2)["info"]["md5"]
    return md5


def add_goods(token, md5, goods_title):
    url3 = "http://erp.fjlonfenner.com/gm-product/api/v4/products"
    cookie = "crx_token=" + token
    Authorization = "Bearer " + token
    headers3 = {
            "Content-Type": "application/json",
            "Cookie": cookie,
            "Authorization": Authorization
        }

    img_sourceUrl = "//cdn-images.x-oss.com/"+md5+"/jpg"
    data3 = {
        "catalogId": None, #None
        "sourceUrl": None,
        "manufacturer": None,
        "brandName": None,
        "currency": "CNY",
        "purchasePrice": None,
        "costPrice": None,
        "salePrice": None,
        "title": goods_title,
        "description": {
            "bulletPoint1": None,
            "bulletPoint2": None,
            "bulletPoint3": None,
            "bulletPoint4": None,
            "bulletPoint5": None,
            "searchTerms": None,
            "textDescription": None
        },
        "images": [
            {
                "purpose": None,
                "sourceUrl": img_sourceUrl,
                "storageKey": md5,
                "seq": 1
            }
        ],
        "status": "ENABLED"
    }

    ss3 = json.dumps(data3)
    r3 = requests.post(url=url3, data=ss3, headers=headers3).content
    return r3




def with_red_title(path):
    with open(path, "r") as f:
        data = f.read()
        s = data.split("\n")
    return s


def batch_add_goods(title_path, imgs_path, interval, img_id=0):
    pathname = imgs_path + "\*.jpg"
    imgs_size = len(glob.glob(pathname=pathname))
    if img_id > imgs_size:
        return
    red = with_red_title(title_path)
    title_size = len(red) * interval
    index = 0
    token = get_token()
    if imgs_size - img_id < title_size:
        title_size = imgs_size - img_id
    for i in range(0, title_size):
        if i % interval == 0 and index < len(red) - 1 and i != 0:
            index += 1
        md5 = up_img(token, i+img_id)
        add_goods(token, md5, red[index])


# if __name__ == '__main__':
#     imgs_path = "F:/untitled7/get_html/imgs"
#     img = update_img_name(imgs_path, "dongwu", aaa)
#     pathname = imgs_path + "\*.jpg"
#     imgs_size = len(glob.glob(pathname=pathname))
#     print(imgs_size)
#     token = get_token()
#     for i in range(imgs_size):
#         md5 = up_img(token, i)
#         add_goods(token, md5, "美丽的塔")
