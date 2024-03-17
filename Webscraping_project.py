import requests
from bs4 import BeautifulSoup
import pandas as pd
import html5lib


html_data= requests.get("https://web.archive.org/web/20200318083015/https://en.wikipedia.org/wiki/List_of_largest_banks").text
soup= BeautifulSoup(html_data,"html.parser")

data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

for row in soup.find_all('tbody')[2].find_all('tr'):
    col = row.find_all('td')
    #Write your code here
    if len(col) > 0:
        name = col[1].text.strip()
        market_cap = float(col[2].string.strip())
        data1=pd.DataFrame({"Name": name, "Market Cap (US$ Billion)": market_cap})
        data = pd.concat([data,data1]ignore_index=True)

print(data)
