import requests
from bs4 import BeautifulSoup

query = "파이썬 강좌"

def get_search_naver_blog(query, start_page=1, end_page=None):
    # 11= (2-1) * 10 + 1 , 
    # 21 = 3

    start = (start_page - 1) * 10 - 1
    url = "https://search.naver.com/search.naver?where=post&sm=tab_jum&query={}&start={}".format(query, start_page)
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")
    lis = bs.select("li.sh_blog_top")

    result = []

    if end_page is None:
        tot_counts = bs.select("span.title_num")[0].text
        tot_counts = tot_counts.split("/")[-1]
        tot_counts = tot_counts.replace("건", "").replace(",", "").strip()
        end_page = tot_counts / 10

        if end_page > 900:
            end_page = 900


    for li in lis:
        try:
            # print(li)
            thumbnail = li.select("img")[0]["src"]
            title = li.select("dl > dt > a")[0]
            summery = li.select("dl > dd.sh_blog_passage")[0].text
            
            title_link = title["href"]
            title_text = title.text

            # print(thumbnail, title_text, title_link, summery)
            # print("*" * 60)

            result.append((thumbnail, title_text, title_link, summery))
        except:
            continue
    

get_search_naver_blog("파이썬강좌", start_page=1, end_page=5)