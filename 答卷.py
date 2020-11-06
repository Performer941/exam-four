import csv
import time
import jsonpath
import requests
from retrying import retry


@retry(stop_max_attempt_number=3)
def main(url, headers):
    # 发送请求
    r = requests.get(url=url, headers=headers)

    info_list = r.json()

    itme_list = jsonpath.jsonpath(info_list, "$.val.props")
    # print(itme_list)
    all_house = []

    for i in itme_list[0]:
        time.sleep(2)
        id = i.get("id")
        region_name = i.get("region_name")
        block_name = i.get("block_name")
        rhval = i.get("rhval")
        area = i.get("area")
        long_title = i.get("long_title")
        comm_name = i.get("comm_name")
        floor_tag = i.get("floor_tag")
        fitment_value = i.get("fitment_value")

        dict0 = {'id': id, 'region_name': region_name, 'block_name': block_name, 'rhval': rhval, 'area': area,
                 'long_title': long_title, 'comm_name': comm_name, 'floor_tag': floor_tag,
                 'fitment_value': fitment_value}

        all_house.append(dict0)
        print(all_house)

    n = r.url
    n = n.replace("https://shuyang.anjuke.com/v3/ajax/map/sale/708/prop_list/?room_num=", "")

    with open("沭阳房产_20201106(%s).csv" % n, "w", encoding="utf-8") as f:
        # 创建一个csv的DictWriter对象，这样才能够将写入csv格式数据到这个文件
        f_csv = csv.DictWriter(f, ['id', 'region_name', 'block_name', 'rhval', 'area',
                                   'long_title', 'comm_name', 'floor_tag', 'fitment_value'])
        # 写入一行（我们用第一行当做表头）
        f_csv.writeheader()
        # 写入多行行（当做数据)
        f_csv.writerows(all_house)


# 捕获异常
def trys(url, headers):
    try:
        main(url, headers)
        r = '成功爬取'
        return r
    except Exception as ret:
        print(ret)
        r = "被发现啦"
        return r


if __name__ == '__main__':
    for i in range(0, 6, 1):
        # time.sleep(10)
        url = "https://shuyang.anjuke.com/v3/ajax/map/sale/708/prop_list/?room_num=%s" % i
        print(url)

        # ip = "106.5.10.206"
        # post = 4221
        #
        # proxies = {
        #   "http": "http://%s:%d" % (ip, post),
        #   "https": "http://%s:%d" % (ip, post)
        # }

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
        }
        r = trys(url, headers)
        print(r)
