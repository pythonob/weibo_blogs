import requests
from lxml import etree
import random, os, re
from urllib.request import HTTPError

def get_header():
    USER_AGENTS = [
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; "
        ".NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; "
        ".NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; "
        ".NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) "
        "Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/60.0.3112.113'
        ' Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2372.400 QQBrowser/9.5.11096.400',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'
    ]
    return {'User-Agent': random.choice(USER_AGENTS)}


def get_xici(): # xici 代理
    proxies = []
    url = 'https://www.xicidaili.com/nn/'
    try:
        resp = requests.get(url, headers = get_header()).text
        html = etree.HTML(resp)
        ip_list = html.xpath('//table[@id="ip_list"]//tr/td[2]/text()')
        port_list = html.xpath('//table[@id="ip_list"]//tr/td[3]/text()')
        type_list = html.xpath('//table[@id="ip_list"]//tr/td[6]/text()')
        length = len(ip_list)

        for i in range(0, length):
            proxy = type_list[i]+"://"+ ip_list[i] + ":" + port_list[i]
            proxies.append(proxy)
        print("raw proxies is produced!")
    except Exception as e:
        print(e)
    return proxies


def get_ip336():
    base_url = 'http://www.ip3366.net/free/?stype=1&page='
    proxies = []
    for i in range(1,11):
        url = base_url+str(i)
        resp = requests.get(url, headers=get_header()).text
        html = etree.HTML(resp)
        ip_list = html.xpath('//table//tr/td[1]/text()')
        port_list = html.xpath('//table//tr/td[2]/text()')
        type_list = html.xpath('//table//tr/td[4]/text()')
        print(len(ip_list))
        for i in range(0,len(ip_list)):
            proxy = type_list[i]+"://"+ip_list[i]+":"+port_list[i]
            proxies.append(proxy)
    return proxies


def clear_proxies(raw_proxies):
    cur_proxy = {}
    for proxy in raw_proxies:
        print("trying {}".format(proxy,))
        cur_proxy["http"] = proxy
        cur_proxy["https"] = proxy
        try:
            resp = requests.get("http://pv.sohu.com/cityjson?ie=utf-8", headers=get_header(), proxies=cur_proxy, timeout=1)
            if resp.status_code == 200:
                print("get it!")
                write(proxy)

        except:
            pass


def write(proxy):
    with open("proxies.txt", "a+",) as f:
        f.write(proxy + "\n")


def clear_old():
    lines = []
    new_lines = []
    with open("proxies.txt", "r") as f:
        lines = f.readlines()
    cur_proxy = {}

    for line in lines:
        cur_proxy["http"] = line
        cur_proxy["https"] = line
        resp = requests.get("http://pv.sohu.com/cityjson?ie=utf-8", headers=get_header(), proxies=cur_proxy, timeout=1)
        if resp.status_code == 200:
            new_lines.append(line)
    with open("proxies.txt", "w") as f:
        for new_line in new_lines:
            f.write(new_line)

if __name__ == '__main__':
    ''' xici 代理质量实在太差了，省了这个吧
    xici_raw =get_xici()
    proxies =clear_proxies(xici_raw)
'''
    clear_old()
    #ip336_raw = get_ip336()  # 悄悄注释掉
    #clear_proxies(ip336_raw) # 悄悄注释掉

