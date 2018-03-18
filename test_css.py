
import requests
import lxml.html

r = requests.get("https://coinmarketcal.com/")
html = r.text
root = lxml.html.fromstring(html)

events = root.cssselect('.content-box')

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
