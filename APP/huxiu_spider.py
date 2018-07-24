import re
import requests
from lxml import etree
import pymysql


# 获取html源码
def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
    res = requests.get(url,headers=headers)
    return res.text

# 获取页面url链接
def get_url(html):
    res = etree.HTML(html)
    url_list = res.xpath('//div[@class="mod-info-flow"]/div/div/h2/a/@href')
    return url_list


# 连续MySQL数据库
def get_mysql(sql,params_list):
    conn = pymysql.connect(host='localhost',port=3306,user='root',password='zly1995422',charset='utf8',db='blog')
    with conn.cursor() as cursor:
        cursor.executemany(sql,params_list)
        conn.commit()

def pattern_regex(html,pattern,flags=re.S):
    html_regex = re.compile(pattern,flags)
    return html_regex.findall(html)

if __name__ == '__main__':
    url = 'https://www.huxiu.com/channel/4.html'
    res = get_html(url)
    url_list = get_url(res)
    html_list = []
    for url in url_list:
        r_url = 'https://www.huxiu.com' + url
        html = get_html(r_url)
        e_html = etree.HTML(html)
        title = e_html.xpath('//div[@class="article-wrap"]/h1/text()')[0]
        if e_html.xpath('//div[@class="article-img-box"]/img/@src'):
            img = e_html.xpath('//div[@class="article-img-box"]/img/@src')[0]
        else:
            img = 'text'
        content = pattern_regex(html,'" class="article-content-wrap">(.*?)<div class="neirong-shouquan-public">')[0]
        html_list.append([title,img,content])
    sql = 'insert into article (title,img,content,type_id)value (%s,%s,%s,13)'
    get_mysql(sql,html_list)