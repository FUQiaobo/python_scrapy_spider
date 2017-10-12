# winlere233
from bs4 import BeautifulSoup
import time
import requests
import lxml
import re 
def xiangxi(url):     #建立抽取页面内容函式
    response_index = requests.get(url)
    soup_index = BeautifulSoup(response_index.text,'lxml')    #加入美丽汤吧！！！
    title_head = soup_index.select('.card-top p i')[0].text    # 提取标题头部
    #print(title_head)
    page_num = soup_index.select('.card-top ul li .num')[0].text    #提取租房价钱
    #print(page_views)
    page_clear = soup_index.select('.card-top span.content')    #提取具体租房信息
    #print(page_clear)
    b = re.compile(u'[0-9]{1,2}[\u4e00-\u9fa5]{1,5}|[\u4e00-\u9fa5]{1,5}')
    c = b.findall(str(page_clear))
    d = c[0]+c[1]+c[2]+','+c[3]+','+c[4]+c[5]+c[6]+c[7]+','+c[8]+'，小区名称：'+c[9]+'。'+'地址：'+c[13]+c[14]
    home_information = '房屋信息：'+page_num+'/月,'+d      #房屋信息与租金
    for i in (title_head,home_information):
        return i
        
        
page = 'http://bj.ganji.com/fang1/'
def lianjie(home_page): #建立获取页面链接与标题的函式
    response_page = requests.get(page)
    soup_page = BeautifulSoup(response_page.text,'lxml')  #加入美丽汤吧！！！
    #print(soup_page)
    soup_href = soup_page.select(' dl > dd.dd-item.title > a ')  #租房首页标题路径
    for k in soup_href:
        if len(k['href']) > 250 :
            page_href = k['href']#查a标签的href值
            page_title = k.string#查a标签的string
            return page_href      #返回链接
            return page_title     #返回首页标题
