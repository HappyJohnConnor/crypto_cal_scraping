import requests
import lxml.html
import MySQLdb

# データベースに接続する
connection = MySQLdb.connect(
    user="scrapingman",
    passwd="dxdutch",
    host="localhost",
    db="crypto_cal_data",
    charset="utf8"
)

cursor = connection.cursor()

# 実行ごとにテーブルを削除する
cursor.execute("DROP TABLE IF EXISTS books")
# テーブル作成
cursor.execute(
    "CREAT TABLE books (time text, title text, sort text, content text)")

r = requests.get("https://coinmarketcal.com/")
html = r.text
root = lxml.html.fromstring(html)

time_of_event = root.xpath(
    "/html/body/main/div[3]/section[1]/div[2]/div[3]/article[1]/div/h5[1]/strong")

print(time_of_event[0].text.strip())
title_of_event = root.xpath(
    "/html/body/main/div[3]/section[1]/div[2]/div[3]/article[1]/div/h5[2]/strong")
print(title_of_event[0].text.strip())
sort_of_event = root.xpath(
    "/html/body/main/div[3]/section[1]/div[2]/div[3]/article[1]/div/h5[3]")
print(sort_of_event[0].text.strip())
content_of_event = root.xpath(
    "/html/body/main/div[3]/section[1]/div[2]/div[3]/article[1]/div/div[1]/p[2]")
print(content_of_event[0].text.strip())


cursor.execute("INSERT INTO books VALUES()")
