import requests
from bs4 import BeautifulSoup

#多摩川河口
url = "http://www1.river.go.jp/cgi-bin/DspWaterData.exe?KIND=9&ID=303051283310010"
res = requests.get(url)

soup = BeautifulSoup(res.content,"html.parser")

frame = soup.findAll("iframe")[0]['src']

url2 = 'http://www1.river.go.jp' + frame

res2 = requests.get(url2)

soup2 = BeautifulSoup(res2.content,"html.parser")

date = soup2.select("body > div > table > tbody > tr:nth-child(1) > td:nth-child(1)")
time = soup2.select("body > div > table > tbody > tr:nth-child(1) > td:nth-child(2)")
waterlevel = soup2.select("body > div > table > tbody > tr:nth-child(1) > td:nth-child(3)")

print(date[0].text)
print(time[0].text)
print(waterlevel[0].text) #text型なので注意

#エラー処理
#閉局や欠測等観測データなしの場合、0.0をセット(influxdbへ投入する際に型混在ができないため)

try:
    floatwaterlevel = float(waterlevel[0].text)
except ValueError as e:
    floatwaterlevel = 0.0

print(floatwaterlevel) #floatとして表示
