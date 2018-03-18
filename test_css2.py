
import requests
import lxml.html
import MySQLdb

connction = MySQLdb.connect(
    user="scrapingman",
    passwd="dxdutch",
    host="localhost",
    db="data_of_crypto_event",
    charset="utf8"
)

cursor = connection.cursor()
cursor.execute(
    "CREATE TABLE books (date text, title text, sort text, content text)")

time_list = []
title_list = []
sort_list = []
content_list = []

r = requests.get("https://coinmarketcal.com/")
html = r.text
root = lxml.html.fromstring(html)

events = root.cssselect('.content-box')

for event in events:
    time_of_event = event.xpath("div/h5[1]/strong")
    print(time_of_event[0].text)

time_of_event = events[0].xpath("div/h5[1]/strong")
print(time_of_event[0].text)

title_of_event = events[0].xpath(
    "div/h5[2]/strong")
print(title_of_event[0].text.strip())

sort_of_event = events[0].xpath(
    "div/h5[3]")
print(sort_of_event[0].text.strip())

content_of_event = events[0].xpath(
    "div/div[1]/p[2]")
print(content_of_event[0].text.strip())
