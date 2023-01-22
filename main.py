import requests, bs4, re
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Title", "URL"]

print("d8888b.  .d8b.  d8888b. .d8888. d88888b d8888b.") 
print("88  `8D d8' `8b 88  `8D 88'  YP 88'     88  `8D ")
print("88oodD' 88ooo88 88oobY' `8bo.   88ooooo 88oobY' ")
print("88~~~   88~~~88 88`8b     `Y8b. 88~~~~~ 88`8b   ")
print("88      88   88 88 `88. db   8D 88.     88 `88. ")
print("88      YP   YP 88   YD `8888Y' Y88888P 88   YD ")


print("created by night3098")

def gethub(url, cssclass, firsturl = 'https://habr.com'):
    habr_urls = {}
    s = requests.get(url)
    b = bs4.BeautifulSoup(s.text, "html.parser")
    p = b.select(cssclass)
    for x in p:
        url = firsturl + x.get('href')
        title = x.span.getText().strip()
        p = '[^0-9a-zA-Zа-яА-Я .:,!-—()_ ЁёьЬъЪ\n\r\t]'
        reg = re.compile(p)
        title=reg.sub('', title)
        habr_urls[url] = title
        table.add_row([title, url])
    return table
    #return title, url
    #return habr_urls

url = 'https://habr.com/ru/hub/python/'
cssclass = '.tm-article-snippet__title-link'
print(gethub(url, cssclass))
