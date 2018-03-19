import datetime
import re

# textを日付型（yyyy-mm-dd）に変える
text = "March 13"
months = ["January", "Febuary", "March", "April", "May",
          "June", "July", "August", "September", "October", "November", "December"]

splited_text = text.split()
print(splited_text)
for i, month in enumerate(months):
    if splited_text[0].find(month) != -1:
        time = datetime.date(2018, i + 1, int(splited_text[1]))
        print(time)
        break
