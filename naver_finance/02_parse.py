import requests
from bs4 import BeautifulSoup as bs


def crawl(code):

    url = f"https://finance.naver.com/item/main.naver?code={code}"
    res = requests.get(url)

    bsobj = bs(res.text, "html.parser")

    div_today = bsobj.find("div", {"class": "today"})
    em = div_today.find("em")
    price = em.find("span", {"class": "blind"})
    # print("가격: " + price.text)

    h_company = bsobj.find("div", {"class": "h_company"})
    a = h_company.find("a")
    # print("회사명: " + a.text)

    div_description = bsobj.find("div", {"class": "description"})
    code = div_description.find("span", {"class": "code"})
    # print("종목코드: " + code.text)

    table_no_info = bsobj.find("table", {"class": "no_info"})
    tds = table_no_info.find_all("td")
    volume = tds[2].find("span", {"class": "blind"})
    # print("거래량: " + volume.text)


    dic = {"price": price.text, "company": a.text, "code": code.text, "volume": volume.text}
    return dic

dic = crawl("035720")
print(dic)