## 目的


[Crytocurrency Calendar][1]のスクレイピング。サイトからそれぞれのイベントの時間、タイトル、種類、内容をとってきて、MySQLに格納する

![[Crytocurrency Calendar][1]](crypto_cal.png){style="display:block;margin-left:auto;margin-right:auto;"}

##　ファイルの説明

### test.py
XPathを用いて一つのイベントから時間、タイトル、種類、内容を持ってくる

### test2.py
XPathの指定を仕方を変えて、test.pyと同じことをする。

### test_convert_to_date.py
サイトから持ってきた時間を、PythonのDate型に変え、さらにstrftime関数を使い、MySQLのDATE型に変換する。

### test_css.py

### test_css2.py

### test_css3.py

## Motivation



## Tests

Describe and show how to run the tests with code examples.

## License

MIT


[1]:https://coinmarketcal.com/
