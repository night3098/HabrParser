import requests, bs4, re
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Title", "URL"]

print("habr.com parser")
print("created by night3098")

def gethub(url, cssclass, firsturl = 'https://habr.com'):
    habr_urls = {}
    s = requests.get(url)")
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
