import requests
from bs4 import BeautifulSoup
import json

KAKAO_TOKEN = "ZRDDHfOWwRF236-UecXtUM4D2XIt3jZldE9ziwo9dZsAAAFw3SNW2g"

'''
curl -v -X POST "https://kapi.kakao.com/v2/api/talk/memo/default/send" \
    -H "Authorization: Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
    -d 'template_object={
        "object_type": "text",
        "text": "텍스트 영역입니다. 최대 200자 표시 가능합니다.",
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
        "button_title": "바로 확인"
    }'

'''
header = ""
def get_gotdeal(keyword):
    url = "https://slickdeals.net/newsearch.php?src=SearchBarV2&q={}&pp=20".format(keyword)

    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")

    rows = bs.select("div.resultRow")

    results = []

    for row in rows:
        link = row.select("a.dealTitle")[0]
        href = link.get("href")
        if href is None:
            continue
        href = "https://slickdeals.net" + href
        title = link.text
        price = row.select("span.price")[0].text.replace("$","").replace("from","").replace(",","").strip()
        if price.find("/") >= 0 or price == "":
            continue
        price = float(price)

        hot = len(row.select("span.icon-fire"))
        results.append((title, href, price, hot))

    return results

print(get_gotdeal("macbook"))
        
