# weibo_blogs
抓取某个用户的全部微博信息，共12万条
依赖的包：scrapy,scrapy_redis,pymysql
1.确定要抓的网址， https://weibo.com 比较难抓，于是考虑移动端的m.weibo.cn,找到要爬的用户的页面，（最开始需要登陆才能打开页面）打开开发者工具，找到获取数
  据的接口，如 'https://m.weibo.cn/api/container/getIndex?containerid=2304132054300185_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page=',
  containerid作为用户的标识，与用户id是两个不同字段，但都能代表用户身份。所以要换个其他用户的微博，只需要吧containerid换掉就行了,page当然就是要抓取的
  页码， 通过这个即可构造要抓取的url
  然后会发现，就算把账号退出，仍然可以直接访问构造好的链接， 所以购买小号的钱竟然省下了。（之前买了一个小号，付了钱却没有发给我账号，亏！）
2.到了这，基本就结束了吧。其他改一下User-Agent , 添加一下代理就可以了
3.添加代理可以另写一个爬虫程序，到代理IP共享的一些网站上去爬，爬完之后，可以用获取到的代理来访问随便一个页面（我用的是
  http://pv.sohu.com/cityjson?ie=utf-8， 可以显示当前ip），如果访问成功，则添加到txt中保存。另外，每次微博爬虫开始前，需要检查一下，原来的txt中的代理
  是否仍然有效。
 
  
