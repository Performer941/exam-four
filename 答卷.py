import json

import requests

url = "https://shuyang.anjuke.com/map/sale/"


# ip = "60.169.134.146"
# post = 4245
#
# proxies = {
#   "http": "http://%s:%d" % (ip, post),
#   "https": "http://%s:%d" % (ip, post)
# }

headers = {
    "user-aengt": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
}

r = requests.get(url=url, headers=headers)

with open("wangye.html", "wb") as f:
    f.write(r.content)


json_str = r.content.decode()

json_dict = json.loads(json_str)



