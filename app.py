
#!urs/bin/env python

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url = 'https://www.jumia.com.gh/electronic-television-video/?q=smart+tv&bcsq=1'
user_agent = UserAgent()

header = {'user-agent', user_agent.chrome}
response = requests.get(url, headers=header)
print(response)
soup = BeautifulSoup(response.content)

item_name = soup.find_all("h3", {"class": "name"})
item_price = soup.find_all("div", {"class": "prc"})
item_discount = soup.find_all("div", {"class": "tag_dsct_sm"})

for name, price, discount in zip(item_name, item_price, item_discount):
    print("Item Name: " + item_name)
    print("Item Price: " + item_price)
    print("Item Discount: " + item_discount)