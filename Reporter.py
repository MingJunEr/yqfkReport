import requests
import json
import re
import os
env_dist = os.environ
if 'username' not in env_dist:
    print('请加入secret')
    exit(1)
r = requests.session()
r.headers = {
    "Referer": "https://app.upc.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fapp.upc.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"

}
r.get("https://app.upc.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fapp.upc.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex")

print(r.post("https://app.upc.edu.cn/uc/wap/login/check", data={"username": env_dist.get('username'), "password": env_dist.get('password')}).text)
t = None

t = r.get("https://app.upc.edu.cn/ncov/wap/default/index").json()

i = t['d']['oldInfo']
#print( t['d'])#
i['date'] = t['d']['info']['date']
i['id'] = t['d']['info']['id']
i['created'] = t['d']['info']['created']
its=r.post("https://app.upc.edu.cn/ncov/wap/default/save",data=i).json()
print(its)
