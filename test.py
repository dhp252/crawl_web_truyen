import requests
from lxml import html
from tqdm import tqdm
from requests_html import HTMLSession

import nest_asyncio

nest_asyncio.apply()

cookies = {
    "metruyenchucom_session":"eyJpdiI6InduWkRMUjM2VFVLTlNRQU9rUk52WXc9PSIsInZhbHVlIjoiYmZnMG0reXZBeVwvREJqTUMyc2JPNG9aSm40M20rbWxOUkZ0RHdLYzNYSEpUb3RyanpQYk1QQkhIMDQ0RDk1YWoiLCJtYWMiOiI4MzMwMTY0NGE5NjcxNDdhNzI4MDVlMGJkZGIwODQ1OGMzNTE4NGUyZGMzNWZkNDgxYmFhMjM4ZGE0ZGQ2NGU5In0%3D",
    "r_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLnRydXllbi5vbmxcL3YyXC9hdXRoXC9sb2dpbiIsImlhdCI6MTY3NTg3MTgzNCwiZXhwIjoxNjc2MzAzODM0LCJuYmYiOjE2NzU4NzE4MzQsImp0aSI6IkZXN1JKTlF5MjJhaTFnZkgiLCJzdWIiOjEzMzIzNzIsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.2PbIa_IxP9AYwMHzYhE37YDyu7GCkVyisG6HP_5GAIQ",
    "l_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLnRydXllbi5vbmxcL3YyXC9hdXRoXC9sb2dpbiIsImlhdCI6MTY3NTg3MTgzNCwiZXhwIjoxNjc2MzAzODM0LCJuYmYiOjE2NzU4NzE4MzQsImp0aSI6IkZXN1JKTlF5MjJhaTFnZkgiLCJzdWIiOjEzMzIzNzIsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.2PbIa_IxP9AYwMHzYhE37YDyu7GCkVyisG6HP_5GAIQ",
    "__cf_bm":"uHE8h3Gk0bjMgnmzTqs1OezLuKmp_Vx1oslSqiVMRls-1675871520-0-AQynpMkjZzOwoEpZKxsGRvvWSz4F7ATE41kjywnfK7fLmWeupMhOp7/U5CuIaKPJKlPoojwuyF3ydvkYkPoKnRgkTebKHo99Lu5xMW2GZ750UlYcaBCLbR3oc+QzG3al5MgILjP27oW/x2gDdgGp78Q=",
    }

session = HTMLSession()


r = session.get('https://metruyencv.com/truyen/vu-luyen-dien-phong/chuong-6008', cookies=cookies, timeout=(10.05, 27))
r.html.render()
r.html.render()
r.html.render()
r.html.render()
content = html.fromstring(r.content)
text = content.xpath('string(//*[@id="article"])').strip()
print(text)
