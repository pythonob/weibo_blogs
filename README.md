# weibo_blogs
<p>抓取某个用户的全部微博信息，共12万条</p>
<p>依赖的包：scrapy,scrapy_redis,pymysql<p>
<pre>
1.确定要抓的网址， https://weibo.com 比较难抓，于是考虑移动端的m.weibo.cn,
  找到要爬的用户的页面，（最开始需要登陆才能打开页面）打开开发者工具，找到获取数据的接口
  结果为，如 'https://m.weibo.cn/api/container/getIndex?containerid=2304132054300185_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page=',
  containerid <font>作为用户的标识，与用户id是两个不同字段，但都能代表用户身份。
  所以要换个其他用户的微博，只需要吧containerid换掉就行了,page当然就是要抓取的页码，通过这个即可构造要抓取的url</font>
  然后会发现，就算把账号退出，仍然可以直接访问构造好的链接。所以不用购买小号，登陆获取cookies等等。

 
