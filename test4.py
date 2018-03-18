import requests
import lxml.html

r = requests.get("https://coinmarketcal.com/")
html = r.text
root = lxml.html.fromstring(html)

events = root.xpath(
    "/html/body/main/div[3]/section[1]/div[2]/div[3]")

print(len(events))
i = 1
tmp = 'article[' + str(i) + ']/div/h5[1]/strong'

# while True:


"""
i = 1
tmp = 'article[' + str(i) + ']/div/h5[1]/strong'
event_of_time = events[0].xpath(tmp)
print(event_of_time[0].text)
"""

"""
time_of_event = event[0].xpath("article[1]/div/h5[1]/strong")
print(time_of_event[0].text)

title_of_event = event[0].xpath(
    "article[1]/div/h5[2]/strong")
print(title_of_event[0].text.strip())

sort_of_event = event[0].xpath(
    "article[1]/div/h5[3]")
print(sort_of_event[0].text.strip())

content_of_event = event[0].xpath(
    "article[1]/div/div[1]/p[2]")
print(content_of_event[0].text.strip())
"""
