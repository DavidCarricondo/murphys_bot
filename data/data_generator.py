import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


response = requests.get('http://www.murphys-laws.com/murphy/murphy-laws.html')
text = BeautifulSoup(response.text)
laws = text.find_all('ul')[1]

laws_list = [e.text for e in laws.find_all('li')]

new_list = []
for e in laws_list:
    temp = e.replace('\t', ' ')
    re.sub(r"(\w*\s){1,2}sent\sby\s(.*?)\s{2,}", "", temp)
    re.sub(r"(\w*\s){1,2}sent\sby\s(.*?)$", "", temp)
    new_list.append(temp)

df = pd.DataFrame({'tweets':new_list})
df.to_csv('data/tweets.csv', index=False)