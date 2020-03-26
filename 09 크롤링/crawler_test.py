'''
1. 원하는 웹페이지에 접속하여 HTML데이터를 받아온다.
2. 받아온 HTML 데이터를 분석가능한 형태로 가공한다.
3. 원하는 데이터를 추출한다.


'''

import requests
from bs4 import BeautifulSoup  #이걸 더 많이씀
from requests_html import HTMLSession

response = requests.get("https://www.naver.com")

# print(response.status_code)
# print(response.headers)
# print(response.text)

# bs = BeautifulSoup(response.text, "html.parser")
# for img in bs.select("img"):
#     print(img)

# session = HTMLSession()
# response = session.get("https://www.naver.com")
# print(response.html.links)

bs = BeautifulSoup(response.text, "html.parser")
for img in bs.select("img"):
    print(img)
for a in bs.select("a"):
    print(a)