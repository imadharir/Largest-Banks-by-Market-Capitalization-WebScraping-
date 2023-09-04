from bs4 import BeautifulSoup
import html5lib
import requests
import pandas as pd

html_data = requests.get("https://web.archive.org/web/20200318083015/https://en.wikipedia.org/wiki/List_of_largest_banks").text
soup= BeautifulSoup(html_data, 'html.parser')

data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

for row in soup.find_all('tbody')[2].find_all('tr')[1:]:
    cols = row.find_all('td')
    myList = []
    for col in cols[1:len(cols)]:
        myList.append(col.text.strip())
    data.loc[len(data)] = myList

data.to_json("bank_market_cap.json")