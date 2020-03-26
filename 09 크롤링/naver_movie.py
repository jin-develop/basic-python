import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/point/af/list.nhn"
r = requests.get(url)
bs = BeautifulSoup(r.text, "lxml")

trs = bs.select("table.list_netizen > tbody > tr")
for tr in trs:
    tds = tr.select("td")
    if len(tds) != 5:
        continue
    number = tds[0].text
    