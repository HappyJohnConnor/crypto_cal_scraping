## 目的


[Crytocurrency Calendar][1]のスクレイピング。サイトからそれぞれのイベントの時間、タイトル、種類、内容をとってきて、MySQLに格納する

![[Crytocurrency Calendar][1]](crypto_cal.png)

<img src="crypto_cal.png" alt="Crytocurrency Calendar" width="300">

##　ファイルの説明

### test.py
XPathを用いて一つのイベントから時間、タイトル、種類、内容を持ってくる

### test2.py
XPathの指定を仕方を変えて、test.pyと同じことをする。

### test_convert_to_date.py
サイトから持ってきた時間を、PythonのDate型に変え、さらにstrftime関数を使い、MySQLのDATE型に変換する。

### test_css.py
Xpathではなく、cssselectを用いて、セレクタ指定でイベントの内容を持ってくる。

### test_css2.py
1つのイベントだけでなく、1ページ中のすべてのイベントを持ってくる。`events = root.cssselect('.content-box')`の際、`events`にはすべてのイベント情報がリスト形式で返ってくる。それぞれの`events`の情報をfor文で回して情報を他のリストに格納する。

### test_css3.py
格納した情報をデータベースに保存する。

## License

MIT


[1]:https://coinmarketcal.com/
